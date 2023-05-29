from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework_bulk import BulkModelViewSet

from  rest_framework.permissions import IsAuthenticated

from orders.models import Orders
from .serializers import OrdersSerializers

class CrudOrders(BulkModelViewSet):
    queryset = Orders.objects.all().select_related('table')
    serializer_class = OrdersSerializers
    model = Orders
    
    def list(self, request, *args, **kwargs):
        orders = self.get_queryset()
        serializer = self.serializer_class(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)