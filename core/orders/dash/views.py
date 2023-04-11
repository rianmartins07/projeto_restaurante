from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.contrib import messages

from core.orders.models import Orders


class CreateOrdersView(LoginRequiredMixin, CreateView):
    model = Orders
    form_class = OrdersForm
    template_name = 'menu/create/index.html'