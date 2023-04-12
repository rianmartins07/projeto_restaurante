
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from menu.models import Menu, FilterMenu
from menu.api.serializers import menuSerializer





class CrudMenu(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    filterset_class = FilterMenu
    filter_backends = [DjangoFilterBackend] 
   