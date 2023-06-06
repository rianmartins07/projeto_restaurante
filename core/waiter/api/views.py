from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action

from waiter.models import Table, FilterTable
from orders.choices import Status
from orders.models import Orders
from waiter.api.serializers import TableSerializers



class CrudTable(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Table.objects.all()
    serializer_class = TableSerializers
    filterset_class = FilterTable
    filter_backends = [DjangoFilterBackend]
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        orders = Orders.objects.filter(table_id=instance.id)

        if orders.exists():
            return Response({'error': 'Existem pedidos nesta mesa, não é possivel deleta-lá.'}, status=status.HTTP_400_BAD_REQUEST)

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.finished = True
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(detail=True, methods=['patch'], url_path='finish')
    def finish_table(self, request, pk=None):
        instance = self.get_object()
        instance.finished = True
        instance.save()
        orders = Orders.objects.filter(table_id=instance.id)
        table = Table.objects.get(id=instance.id)
        print(table.finished)
        if not table.finished:
            for order in orders:
                if order.status != Status.PRONTO and order.status != Status.CANCELADO:
                    print(order.status, Status.PRONTO)
                    return Response({'error': 'Existem pedidos em aberto para esta mesa.'}, status=400)
            
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        else:
             return Response({'error': 'A mesa ja está finalizada!'}, status=400)
        return Response(serializer.errors, status=400)
