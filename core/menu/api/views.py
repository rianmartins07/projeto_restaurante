
from rest_framework import viewsets
from  rest_framework.permissions import IsAuthenticated


from menu.models import Menu
from menu.api.serializers import menuSerializer





class CrudMenu(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

    