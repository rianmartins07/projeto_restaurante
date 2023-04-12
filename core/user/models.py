from django.db import models
import django_filters as filters

from .choices import Sexo, Role
# Create your models here.




class User(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=81, verbose_name='user')
    nome = models.CharField(max_length=81, verbose_name='nome')
    cpf = models.CharField(max_length=11, verbose_name='cpf', unique=True)
    email = models.EmailField('endereco de email', unique=True)
    role = models.CharField(max_length=30, choices=Role.choices)
    sexo = models.CharField(max_length=20, choices=Sexo.choices)
    data_nascimento = models.DateField(verbose_name='data de nascimento')
    numero_celular = models.CharField(max_length=15, verbose_name='numero de celular')
    
    class Meta:
        managed = True
        app_label = 'user'
    
    def clean(self):
        # Remove caracteres não numéricos do campo CPF
        self.cpf = ''.join(filter(str.isdigit, self.cpf))
        # Atualiza o valor do campo CPF no objeto do modelo
        self.cpf = self.cpf.replace('.', '').replace('-', '')

    def save(self, *args, **kwargs):
        self.clean()  # Chama o método clean() para validar e limpar o campo CPF
        super(User, self).save(*args, **kwargs)
        
        
class UserFilter(filters.FilterSet):
    nome__icontains = filters.CharFilter(field_name='nome', lookup_expr='icontains')
    numero_celular__icontains = filters.CharFilter(field_name='numero_celular', lookup_expr='icontains')
    email__icontains = filters.CharFilter(field_name='email', lookup_expr='icontains')
    role__icontains = filters.CharFilter(field_name='role', lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['nome', 'numero_celular', 'email', 'role']