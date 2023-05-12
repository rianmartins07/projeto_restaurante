from django.db.models import fields
from rest_framework_bulk import BulkSerializerMixin, BulkListSerializer
from rest_framework import serializers
from pycpfcnpj import cpfcnpj


from orders.models import Orders
class OrdersSerializers (BulkSerializerMixin, serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Orders
        app_label = 'waiter'
        list_serializer_class = BulkListSerializer