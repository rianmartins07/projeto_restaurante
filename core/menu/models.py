from django.db import models
import django_filters as filters
# Create your models here.

class CustomMenu(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, verbose_name='nome do prato')
    valor = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='valor do prato')
    descricao = models.TextField(verbose_name='descrição do prato')
    foto = models.ImageField(verbose_name='foto do prato')
    status = models.CharField(verbose_name='ativo ou inativo', max_length=10)
    
    class Meta:
        managed = True
        app_label = 'menu'

class FilterMenu (filters.FilterSet):
    nome__icontains = filters.CharFilter(field_name='nome', lookup_expr='icontains')
    
    class Meta:
        model = CustomMenu
        fields = ['nome']