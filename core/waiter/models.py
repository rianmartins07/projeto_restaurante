from django.db import models
import django_filters as filters

# Create your models here.
class Table(models.Model):
    id = models.AutoField(primary_key=True)
    responsible_name = models.CharField(max_length=81, verbose_name='nome do responsavel da mesa')
    table_number = models.CharField(max_length=81, verbose_name='numero que vai na mesa')
    finished = models.BooleanField(verbose_name='Se a mesa esta finalizada ou não', default=False)
    class Meta:
        db_table = 'table_tables'
        managed = True
        app_label = 'waiter'

class FilterTable (filters.FilterSet):
    table_number__icontains = filters.CharFilter(field_name='table_number', lookup_expr='icontains')
    
    class Meta:
        model = Table
        fields = ['table_number']