from django.template import loader
from django.http import HttpResponse

def create_user(request):
    template_name = loader.get_template('user/create/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))

def update_user (request):
    template_name = loader.get_template('user/update/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))

def list_user (request):
    template_name = loader.get_template('user/list/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))

def feedback_user (request):
    template_name = loader.get_template('user/feedback/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))

def reports_user (request):
    template_name = loader.get_template('user/reports/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))

def reports_customers_user (request):
    template_name = loader.get_template('user/reports/customers/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))

def reports_requests_user (request):
    template_name = loader.get_template('user/reports/requests/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))

def reports_sales_user (request):
    template_name = loader.get_template('user/reports/sales/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))

def reports_time_course_user (request):
    template_name = loader.get_template('user/reports/time/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))

def  reports_time_user(request):
    template_name = loader.get_template('user/reports/time-course/index.html')
    context = dict()

    return HttpResponse(template_name.render(context, request))