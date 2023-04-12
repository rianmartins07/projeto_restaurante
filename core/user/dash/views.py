from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.contrib import messages


from .forms import UserForm
from user.models import User


class UpdateUser(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'user/update/index.html'

class CreateUserView(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = 'user/create/index.html'
    


@login_required(login_url=reverse_lazy('login'))
def list_user (request):
    template_name = loader.get_template('user/list/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))

@login_required(login_url=reverse_lazy('login'))
def feedback_user (request):
    template_name = loader.get_template('user/feedback/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))

@login_required(login_url=reverse_lazy('login'))
def reports_user (request):
    template_name = loader.get_template('user/reports/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))

@login_required(login_url=reverse_lazy('login'))
def reports_customers_user (request):
    template_name = loader.get_template('user/reports/customers/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))

@login_required(login_url=reverse_lazy('login'))
def reports_requests_user (request):
    template_name = loader.get_template('user/reports/requests/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))

@login_required(login_url=reverse_lazy('login'))
def reports_sales_user (request):
    template_name = loader.get_template('user/reports/sales/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))

@login_required(login_url=reverse_lazy('login'))
def reports_time_course_user (request):
    template_name = loader.get_template('user/reports/time/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))

@login_required(login_url=reverse_lazy('login'))
def  reports_time_user(request):
    template_name = loader.get_template('user/reports/time-course/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))


@login_required(login_url=reverse_lazy('login'))
def  reports_time_user(request):
    
    template_name = loader.get_template('account/login')
    context = dict()

    return HttpResponse(template_name.render(context, request))
