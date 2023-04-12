from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.contrib import messages



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

@login_required(login_url=reverse_lazy('login'))
def tables_operator (request):
    template_name = loader.get_template('operator/tables-operator/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))