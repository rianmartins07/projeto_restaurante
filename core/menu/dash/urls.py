from django.urls import re_path
from django.urls import path, include

from menu.dash.views import *

urlpatterns = [
    re_path(r'create/$', CreateMenuView.as_view(), name='create_user'),
    re_path(r'(?P<pk>[0-9]+)/update/$', UpdateMenuView.as_view(), name='update'),
    re_path(r'dish/$', dish_menu, name='dish'),
    re_path(r'list/$', view_menu, name='list_menu'),
]
