from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserChangeForm
from django.http import QueryDict

from user.models import User, UserFilter
from .serializers import userSerializer


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = '__all__'
        # Se houver algum campo que você não deseja exibir ou permitir que seja atualizado, você pode excluí-lo da lista fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].required = False  # Torna o campo de senha não obrigatório

class CrudUser(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = User.objects.all()
    serializer_class = userSerializer
    filterset_class = UserFilter
    filter_backends = [DjangoFilterBackend]
    form_class = CustomUserChangeForm

    def create(self, request, *args, **kwargs):
        if request.method == 'POST':
            cpf = request.data.get('cpf')
            email = request.data.get('email')
            id = request.data.get('groups')
            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')
            sexo = request.data.get('sexo')
            numero_celular = request.data.get('numero_celular')
            
            
            if not Group.objects.get(id=id):
                raise serializer.ValidationError('Escolha um cargo!')
            user = User.objects.create_user(cpf=cpf, email=email, first_name=first_name,last_name=last_name, sexo=sexo, numero_celular=numero_celular)
            group = Group.objects.get(id=id)
            group.user_set.add(user)
            
            permissions_by_group = group.permissions.all()
            for permission in permissions_by_group:
                user.user_permissions.add(permission)

            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            


    def perform_update(self, serializer):
        user = serializer.instance
        old_password = self.request.data.get('old_password')
        new_password = self.request.data.get('new_password')
        confirm_password = self.request.data.get('confirm_password')

        if new_password or confirm_password:
            if old_password:
                if not user.check_password(old_password):
                    raise serializer.ValidationError('A senha antiga fornecida está incorreta.')
            else:
                raise serializer.ValidationError('É necessário fornecer a senha antiga.')

            if new_password != confirm_password:
                raise serializer.ValidationError('A nova senha e a confirmação não correspondem.')

            if new_password:
                user.set_password(new_password)
        else:
            user.save()
        super().perform_update(serializer)
        
        return user