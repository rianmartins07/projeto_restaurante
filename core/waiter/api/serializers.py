from django.db.models import fields
from rest_framework import serializers

from waiter.models import Table

class TableSerializers(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'
        app_label = 'waiter'
