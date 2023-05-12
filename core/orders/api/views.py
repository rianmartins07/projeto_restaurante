from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework_bulk import BulkModelViewSet

from  rest_framework.permissions import IsAuthenticated

from orders.models import Orders
from .serializers import OrdersSerializers

class CrudOrders(BulkModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializers
    model = Orders
    