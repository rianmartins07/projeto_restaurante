from django.db import models
from user.models import User as customUser
from menu.models import CustomMenu as customMenu
from waiter.models import Table
# Create your models here.






class Orders(models.Model):
    id_order = models.AutoField(primary_key=True, verbose_name='chave primaria id order')
    waiter_id = models.ForeignKey(customUser, verbose_name='chave estrangeira garçom',on_delete=models.CASCADE)
    dish_id = models.ForeignKey(customMenu, verbose_name='chave estrangeira prato', on_delete=models.CASCADE)
    quantity = models.IntegerField(max_length=10, verbose_name='quantidade', default=1)
    datetime = models.DateTimeField(auto_now=True, auto_now_add=True)
    table_id = models.ForeignKey(Table, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'orders'
        managed = True
        app_label = 'core'

