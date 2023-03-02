from django.template import loader
from django.http import HttpResponse

def create_menu(request):
    template_name = loader.get_template('menu/create/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))

def update_menu(request):
    template_name = loader.get_template('menu/update/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))

def dish_menu(request):
    template_name = loader.get_template('menu/dish/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))

def view_menu (request):
    template_name = loader.get_template('menu/index.html')
    context = dict()  

    return HttpResponse(template_name.render(context, request))