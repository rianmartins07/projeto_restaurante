from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

@login_required(login_url=reverse_lazy('login'))
def create_menu(request):
    template_name = loader.get_template('menu/create/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))

@login_required(login_url=reverse_lazy('login'))
def update_menu(request):
    template_name = loader.get_template('menu/update/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))

@login_required(login_url=reverse_lazy('login'))
def dish_menu(request):
    template_name = loader.get_template('menu/dish/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))

@login_required(login_url=reverse_lazy('login'))
def view_menu (request):
    template_name = loader.get_template('menu/index.html')
    context = dict()  

    return HttpResponse(template_name.render(context, request))