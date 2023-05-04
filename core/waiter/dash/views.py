from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.contrib import messages

from waiter.models import Table
from .forms import TableForm

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


class CreateTable (LoginRequiredMixin, CreateView):
    form_class = TableForm
    model = Table
    template_name = 'operator/tables-operator/index.html'

class UpdateTable(LoginRequiredMixin, UpdateView):
    form_class=TableForm
    model = Table
    template_name = 'orders/create/index.html'