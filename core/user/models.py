from django.db import models

# Create your models here.



class User(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=81, verbose_name='nome')
    cpf = models.CharField(max_length=11, verbose_name='cpf')
    email = models.EmailField('endereco de email', unique=True)

    class sexo (models.TextChoices):
        MASCULINO = 'Masculino'
        FEMININO = 'Feminino'
        PREFIRO_NAO_DIZER = 'Prefiro não dizer'

    sexo = models.CharField(max_length=20, choices=sexo.choices)
    data_nascimento = models.DateField(verbose_name='data de nascimento')
    numero_celular = models.CharField(max_length=15, verbose_name='numero de celular')
    
