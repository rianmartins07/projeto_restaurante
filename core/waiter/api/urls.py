from django.urls import re_path, include
from rest_framework import routers

from waiter.api.views import CrudTable

app_name = 'api_waiter'

api_router = routers.DefaultRouter()
api_router.register(r"table", CrudTable)

urlpatterns = [
    re_path(r'',include(api_router.urls))
]