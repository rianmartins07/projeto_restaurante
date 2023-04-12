from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView


from menu.models import Menu
from menu.dash.forms import MenuForm


class CreateMenuView(LoginRequiredMixin, CreateView):
    model = Menu
    form_class = MenuForm
    template_name = 'menu/create/index.html'
    
    def get_context_data(self, **kwargs):
        context = super(CreateMenuView, self).get_context_data(**kwargs)
        context['is_create'] = True
        
        return context
    
class UpdateMenuView(LoginRequiredMixin, UpdateView):
    model = Menu
    form_class = MenuForm
    template_name = 'menu/update/index.html'



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