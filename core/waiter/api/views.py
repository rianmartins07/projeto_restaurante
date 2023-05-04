from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from waiter.models import Table
from waiter.api.serializers import TableSerializers





class CrudTable(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Table.objects.all()
    serializer_class = TableSerializers