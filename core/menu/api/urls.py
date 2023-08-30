from django.urls import re_path, include
from rest_framework import routers

from menu.api.views import CrudMenu

app_name = 'api_menu'

api_router = routers.DefaultRouter()
api_router.register(r"info", CrudMenu)

urlpatterns = [
    re_path(r'',include(api_router.urls))
]