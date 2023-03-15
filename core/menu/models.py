from django.db import models

# Create your models here.

class menu(models.Model):
    id = models.IntegerField(auto_created=True, db_index=True, primary_key=True)
    nome = models.CharField(max_length=255, verbose_name='nome do prato')
    valor = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='valor do prato')
    descricao = models.TextField(verbose_name='descrição do prato')
    foto = models.ImageField(verbose_name='foto do prato')
    status = models.BooleanField(verbose_name='ativo ou inativo')
    