from django.db.models import fields
from rest_framework import serializers

from waiter.models import Table

class TableSerializers (serializers.ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = Table
        app_label = 'waiter'