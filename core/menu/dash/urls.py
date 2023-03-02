from django.urls import re_path
from django.urls import path, include

from core.menu.dash.views import *

urlpatterns = [
    re_path(r'create/$', create_menu, name='create'),
    re_path(r'update/$', update_menu, name='update'),
    re_path(r'dish/$', dish_menu, name='dish'),
    re_path(r'view_menu/$', view_menu, name='view_menu'),
]
