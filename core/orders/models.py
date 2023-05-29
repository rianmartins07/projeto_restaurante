from django.db import models
from user.models import User as customUser
from menu.models import CustomMenu as customMenu
from waiter.models import Table
from orders.choices import *
# Create your models here.


class Orders(models.Model):
    id_order = models.AutoField(primary_key=True, verbose_name='chave primaria id order')
    waiter = models.ForeignKey(customUser, verbose_name='chave estrangeira garçom',on_delete=models.CASCADE)
    dish = models.ForeignKey(customMenu, verbose_name='chave estrangeira prato', on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='quantidade', default=1)
    datetime = models.DateTimeField(auto_now_add=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=Status.choices, default=Status.PEDIDO_NA_COZINHA)
    canceled_by = models.CharField(max_length=255,null=True, default=None)
    class Meta:
        db_table = 'table_orders'
        managed = True
        app_label = 'orders'

class Feedback(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=30, choices=FeedbackChoices.choices)
    
    class Meta:
        db_table = 'table_feedback'
        managed = True
        app_label = 'orders'



