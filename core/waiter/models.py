from django.db import models

# Create your models here.
class Table(models.Model):
    id = models.AutoField(primary_key=True)
    responsible_name = models.CharField(max_length=81, verbose_name='nome do responsavel da mesa')
    table_number = models.CharField(max_length=81, verbose_name='numero que vai na mesa')
    class Meta:
        managed = True
        app_label = 'waiter'

