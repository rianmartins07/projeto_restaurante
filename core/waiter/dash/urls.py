from django.urls import re_path
from django.urls import path, include

from waiter.dash.views import CreateTable, overview, requests

app_name='waiter'

urlpatterns = [
    re_path(r'overview/', overview , name='cashies_overview'),
    re_path(r'requests/', requests , name='cashies_requests'),
    re_path(r'tables_operator/', CreateTable.as_view() , name='cashies_overview'),
]
