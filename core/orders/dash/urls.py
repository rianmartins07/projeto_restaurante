from django.urls import re_path
from django.urls import path, include

from orders.dash.views import *

app_name='orders'

urlpatterns = [
    re_path(r'(?P<pk>[0-9]+)/create/', CreateOrder.as_view(), name='create_order'),
    re_path(r'list/cook/', list_cook, name='list_cook_orders'), #visão do cozinheiro dos pedidos que chegam para ele
    re_path(r'list/requests/', list_requests, name='list_requests'),
    re_path(r'list/requests_finished/', requests_progress, name='requests_in_progress'),
    re_path(r'update/', update_order, name='update_order'),
    re_path(r'list/requests_inprogress/', cook_table, name='cook-table'),
]
