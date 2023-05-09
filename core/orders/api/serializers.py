from django.db.models import fields
from rest_framework import serializers
from pycpfcnpj import cpfcnpj


from orders.models import Orders
class OrdersSerializers (serializers.ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = Orders
        app_label = 'waiter'