from django.urls import re_path, include
from rest_framework import routers

from user.api.views import *

app_name = 'api_user'

api_router = routers.DefaultRouter()
api_router.register(r"info", CrudUser)

urlpatterns = [
    re_path(r'',include(api_router.urls))
]