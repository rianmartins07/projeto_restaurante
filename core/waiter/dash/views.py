from typing import Any, Dict
from django import http
from django.http.response import HttpResponse
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.core.exceptions import PermissionDenied

from waiter.models import Table
from .forms import TableForm

class CreateTable (LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'waiter.add_table'
    form_class = TableForm
    model = Table
    template_name = 'operator/tables-operator/index.html'
    
    def get_context_data(self, **kwargs):
        context = super(CreateTable, self).get_context_data(**kwargs)
        tables = Table.objects.all()
        context['tables'] = tables
        return context
        

class UpdateTable(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required='waiter.change_table'
    form_class=TableForm
    model = Table
    template_name = 'orders/create/index.html'



@login_required(login_url=reverse_lazy('login'))
def overview (request):
    template_name = loader.get_template('operator/overview/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))

@login_required(login_url=reverse_lazy('login'))
def requests (request):
    template_name = loader.get_template('operator/requests/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))


