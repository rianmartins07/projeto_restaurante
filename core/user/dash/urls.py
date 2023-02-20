from django.urls import re_path
from django.urls import path, include

from core.user.dash.views import *

urlpatterns = [
    re_path(r'create/', create_user, name='create'),
    re_path(r'update/', update_user, name='update'),
    re_path(r'list/', list_user, name='update'),
    re_path(r'feedback/', feedback_user, name='update'),
    re_path(r'reports/$', reports_user, name='reports'),
    re_path(r'reports/customers/', reports_customers_user, name='customers'),
    re_path(r'reports/requests/', reports_requests_user, name='requests'),
    re_path(r'reports/sales/', reports_sales_user, name='sales'),
    re_path(r'reports/time_course/', reports_time_course_user, name='time_course'),
    re_path(r'reports/time/', reports_time_user, name='time'),
]
