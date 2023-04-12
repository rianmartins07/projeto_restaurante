from django.db import models
from user.models import User as customUser
from menu.models import CustomMenu as customMenu
# Create your models here.



class Cliente(models.Model):
    id_client = models.AutoField(primary_key=True, verbose_name='chave identificadora de cliente')
    client_name = models.CharField(max_length=81, verbose_name='nome do cliente')
    
    class Meta:
        db_table = 'client'
        managed = True
        app_label = 'core'



class Orders(models.Model):
    id_order = models.AutoField(primary_key=True, verbose_name='chave primaria id order')
    waiter_id = models.ForeignKey(customUser, verbose_name='chave estrangeira garçom',on_delete=models.CASCADE)
    dish_id = models.ForeignKey(customMenu, verbose_name='chave estrangeira prato', on_delete=models.CASCADE)
    quantity = models.IntegerField(max_length=10, verbose_name='quantidade', default=1)
    datetime = models.DateTimeField(auto_now=True, auto_now_add=True)
    client_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'orders'
        managed = True
        app_label = 'core'

