from django.urls import re_path, include
from rest_framework import routers
from rest_framework_bulk.routes import BulkRouter


from .views import CrudOrders


app_name = 'api_orders'

router = BulkRouter()
router.register(r'', CrudOrders)

urlpatterns = [
    re_path(r'',include(router.urls))
]