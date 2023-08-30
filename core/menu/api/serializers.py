from django.db.models import fields
from rest_framework import serializers


from menu.models import CustomMenu


class menuSerializer(serializers.ModelSerializer):
    foto_url = serializers.SerializerMethodField()
    
    def get_foto_url(self, obj):
        
        request = self.context.get('request')
        if obj.foto:
            return request.build_absolute_uri(obj.foto.url)
        else:
            return None

    class Meta:
        app_label= 'menu'
        model = CustomMenu
        fields = '__all__'
        