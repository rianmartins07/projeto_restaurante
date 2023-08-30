from django.db import models
import django_filters as filters
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
import string


from .choices import Sexo
import string
import copy
import random

class UserManager(BaseUserManager):
    def generate_random_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    
    def create_user(self, cpf, password=None, superuser=False, **extra_fields):
        user = self.model(cpf=cpf, **extra_fields)  # Adicione o parâmetro 'superuser'

        if not cpf:
            raise ValueError('O campo CPF é obrigatório.')
        
        
        if not superuser:
            password = self.generate_random_password()
            context = {
                'password': password,
            }
            message = render_to_string('utils/passwordEmail.html', context)
            send_mail(
                'Bem-vindo ao nosso site! {}'.format(user.get_full_name().upper()),
                '',
                'lprsystembr@gmail.com',  # Email remetente
                [user.email],  # Email destinatário
                html_message=message,
                fail_silently=False,
            )
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    

    def create_superuser(self, cpf, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given CPF and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(cpf, password, superuser=True, **extra_fields)
        

class User(AbstractUser):
    objects = UserManager()
    cpf = models.CharField(max_length=11, verbose_name='cpf', unique=True)
    email = models.EmailField('endereco de email', unique=True)

    sexo = models.CharField(max_length=20, choices=Sexo.choices)
    data_nascimento = models.DateField(verbose_name='data de nascimento', blank=False, null=False, default="1900-10-10")
    numero_celular = models.CharField(max_length=15, verbose_name='numero de celular')
    
    username = None
    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['email']
    
    class Meta(AbstractUser.Meta):
        permissions = (("generate_report", "can generate and view report"),)
        swappable = 'AUTH_USER_MODEL'
        db_table = 'auth_user'
        verbose_name = 'user user'


class UserFilter(filters.FilterSet):
    first_name__icontains= filters.CharFilter(field_name='first_name', lookup_expr='icontains')
    numero_celular__icontains = filters.CharFilter(field_name='numero_celular', lookup_expr='icontains')
    email__icontains = filters.CharFilter(field_name='email', lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['first_name', 'numero_celular', 'email']
