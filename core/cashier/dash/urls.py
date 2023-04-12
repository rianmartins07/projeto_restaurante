from django.urls import re_path
from django.urls import path, include

from cashier.dash.views import *

app_name='cashier'

urlpatterns = [
    re_path(r'overview/', overview , name='cashies_overview'),
    re_path(r'requests/', requests , name='cashies_requests'),
    re_path(r'tables_operator/', tables_operator , name='cashies_overview'),
]
