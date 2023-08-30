from typing import Any
from django import http
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import F
from django.http import HttpResponse
from django.http.response import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from menu.models import CustomMenu
from orders.models import Orders
from waiter.models import Table
from django.core.exceptions import PermissionDenied

class CreateOrder (LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    fields = '__all__'
    model = Orders
    template_name = 'orders/create/index.html'
    permission_required = 'orders.add_orders'
    
   
    def get_context_data(self, **kwargs):
        context = super(CreateOrder, self).get_context_data(**kwargs)
        id = int(self.request.path.split('/')[3])
        obj = Table.objects.get(pk=id)
        menu = CustomMenu.objects.all()
        
        orders_by_table = Orders.objects.filter(table_id=id).select_related('dish').annotate(
            total_value=F('dish__valor')*F('quantity')
        )

        context['menu'] = menu
        context['table_id'] = obj.id
        context['table_number'] = obj.table_number
        context['responsible'] = Table.objects.get(pk=id).responsible_name
        context['orders_by_table'] = orders_by_table if orders_by_table else None
        
        return context

class UpdateOrder (LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    fields = '__all__'
    model = Orders
    template_name = 'orders/list_cook_orders/index.html'
    permission_required = 'orders.view_orders', 'orders.delete_orders'
    
    def get_context_data(self, **kwargs):
        context = super(UpdateOrder, self).get_context_data(**kwargs)
        context['order'] = Orders.objects.get(id_order=self.kwargs['pk'])
        return context        
        

@login_required(login_url=reverse_lazy('login'))
def feedback_user (request):
    if request.user.has_perm('user.view_feedback', 'user.add_feedback'):
        template_name = loader.get_template('orders/feedback/index.html')
    else:
        raise PermissionDenied
    
    context = dict()

    return HttpResponse(template_name.render(context, request))

@login_required(login_url=reverse_lazy('login'))
def list_cook (request):
    if request.user.has_perm('user.view_orders'):
        template_name = loader.get_template('orders/list_cook_orders/index.html')
    else:
        raise PermissionDenied
    context = dict()

    return HttpResponse(template_name.render(context, request))

@login_required(login_url=reverse_lazy('login'))
def list_requests (request):
    if request.user.has_perm('user.view_orders'):
        template_name = loader.get_template('orders/list_requests/index.html')
    else:
        raise PermissionDenied
    context = dict()

    return HttpResponse(template_name.render(context, request))

@login_required(login_url=reverse_lazy('login'))
def requests_progress (request):
    if request.user.has_perm('user.view_orders'):
        template_name = loader.get_template('orders/orders-in-progress/index.html')
    else:
        raise PermissionDenied
    
    context = dict()

    return HttpResponse(template_name.render(context, request))


@login_required(login_url=reverse_lazy('login'))
def cook_table (request):
    template_name = loader.get_template('cook/tables-cook/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))


