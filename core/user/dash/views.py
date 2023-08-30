from typing import Any, Dict
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.hashers import make_password
from django.core.exceptions import PermissionDenied
from django.db.models import F, ExpressionWrapper, DecimalField, Sum

from .forms import UserForm
from user.models import User
from orders.models import Orders

class UpdateUser(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    permission_required = 'user.change_user'
    model = User
    form_class = UserForm
    template_name = 'user/update/index.html'
    
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['is_administrador'] = self.request.user.groups.first().name == 'Administrador'
        context['current_user'] = self.request.user
        
        return context


class CreateUserView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = User
    permission_required = 'user.add_user'
    form_class = UserForm
    template_name = 'user/create/index.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['is_administrador'] = self.request.user.groups.first().name == 'Administrador'
        return context

@login_required(login_url=reverse_lazy('login'))
def list_user (request):
    if request.user.has_perm('user.view_user'):
        template_name = loader.get_template('user/list/index.html')
    else:
        raise PermissionDenied
    context = dict()
    
    return HttpResponse(template_name.render(context, request))



@login_required(login_url=reverse_lazy('login'))
def reports_user (request):
    print(list(request.user.groups.all())[0])
    if request.user.has_perm('user.generate_report_and_view_report'):
        template_name = loader.get_template('user/reports/index.html')    
    else:
        raise PermissionDenied
    context = dict()
    
    return HttpResponse(template_name.render(context, request))

@login_required(login_url=reverse_lazy('login'))
def reports_customers_user (request):
    if request.user.has_perm('user.generate_report'):
        template_name = loader.get_template('user/reports/customers/index.html')    
    else:
        raise PermissionDenied
    context = dict()

    return HttpResponse(template_name.render(context, request))

@login_required(login_url=reverse_lazy('login'))
def reports_requests_user (request):
    if request.user.has_perm('user.generate_report'):
        template_name = loader.get_template('user/reports/requests/index.html')    
    else:
        raise PermissionDenied
    context = dict()

    return HttpResponse(template_name.render(context, request))

@login_required(login_url=reverse_lazy('login'))
def reports_sales_user (request):
    if request.user.has_perm('user.generate_report'):
        template_name = loader.get_template('user/reports/sales/index.html')    
    else:
        raise PermissionDenied
    context = {}
    context['orders'] = Orders.objects.all().select_related('dish').annotate(
            total_value=F('dish__valor')*F('quantity')
        )
    total_amount = Orders.objects.all().select_related('dish').aggregate(
        total_amount = ExpressionWrapper(Sum(F('quantity') * F('dish__valor')), output_field=DecimalField())
    )['total_amount']
    
    context['total_amount'] = total_amount
    return HttpResponse(template_name.render(context, request))

@login_required(login_url=reverse_lazy('login'))
def reports_time_course_user (request):
    if request.user.has_perm('user.generate_report'):
        template_name = loader.get_template('user/reports/time/index.html')    
    else:
        raise PermissionDenied
    context = dict()

    return HttpResponse(template_name.render(context, request))

@login_required(login_url=reverse_lazy('login'))
def  reports_time_user(request):
    if request.user.has_perm('user.generate_report'):
        template_name = loader.get_template('user/reports/time-course/index.html')    
    else:
        raise PermissionDenied
    context = dict()

    return HttpResponse(template_name.render(context, request))

