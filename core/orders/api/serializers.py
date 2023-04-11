from django.db.models import fields
from rest_framework import serializers
from pycpfcnpj import cpfcnpj

from user.models import *


class userSerializer (serializers.ModelSerializer):
    

   
    def validate_cpf (self, value):
        if not cpfcnpj.validate(value):
            raise serializers.ValidationError("CPF inserido incorretamente.")
        return value

    
    class Meta:
        app_label = 'user'
        model= User
        fields= '__all__'