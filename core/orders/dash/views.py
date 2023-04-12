from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.contrib import messages

from orders.models import Orders


@login_required(login_url=reverse_lazy('login'))
def orders_create (request):
    template_name = loader.get_template('orders/create/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))

@login_required(login_url=reverse_lazy('login'))
def list_cook (request):
    template_name = loader.get_template('orders/list_cook_orders/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))

@login_required(login_url=reverse_lazy('login'))
def list_requests (request):
    template_name = loader.get_template('orders/list_requests/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))

@login_required(login_url=reverse_lazy('login'))
def requests_progress (request):
    template_name = loader.get_template('orders/orders-in-progress/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))

@login_required(login_url=reverse_lazy('login'))
def update_order (request):
    template_name = loader.get_template('orders/update-order/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))

@login_required(login_url=reverse_lazy('login'))
def cook_table (request):
    template_name = loader.get_template('cook/tables-cook/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))

from django.urls import get_resolver

