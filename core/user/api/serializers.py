from django.db.models import fields
from rest_framework import serializers
from pycpfcnpj import cpfcnpj

from user.models import *


class userSerializer (serializers.ModelSerializer):
    email = serializers.EmailField(read_only=True)
    cpf = serializers.EmailField(read_only=True)
    full_name = serializers.SerializerMethodField()
    group_name = serializers.SerializerMethodField()
    
    def get_group_name(self, obj):
        if self.context['request'].method == 'GET':
            if obj.groups.exists():
                group = obj.groups.first()
                group_pk = group.pk
                return Group.objects.get(id=group_pk).name

        return None
    
    def get_full_name(self, obj):
        if self.context['request'].method == 'GET':
            return f"{obj.first_name} {obj.last_name}"
        
        return None
    
    def validate_cpf (self, value):
        if not cpfcnpj.validate(value):
            raise serializers.ValidationError("CPF inserido incorretamente.")
        return value

    
    class Meta:
        app_label = 'user'
        model= User
        fields= '__all__'