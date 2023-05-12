from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.db.models import F

from waiter.models import Table
from orders.models import Orders
from menu.models import CustomMenu


class CreateOrder (LoginRequiredMixin, CreateView):
    fields = '__all__'
    model = Orders
    template_name = 'orders/create/index.html'
    

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


