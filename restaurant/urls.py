"""restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings

from drf_yasg import openapi
from drf_yasg.views import get_schema_view


urlpatterns_API = [
    path('api/user/', include('core.user.api.urls')),
    path('api/menu/', include('core.menu.api.urls')),
    path('api/waiter/', include('core.waiter.api.urls')),
]

schema_view = get_schema_view(
    openapi.Info(

        title="LBPR System",

        default_version='v1',

        description="Test description",
    ),
    patterns=urlpatterns_API,
    public=True,
)

urlpatterns = [
    path(r'api/', login_required(schema_view.with_ui('swagger', cache_timeout=0)), name='schema-swagger-ui' ),
    path('admin/', login_required(admin.site.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
    path(r'home/user/', include('core.user.dash.urls'),name='user'),
    path(r'home/menu/', include('core.menu.dash.urls'), name='menu'),
    path(r'home/waiter/', include('core.waiter.dash.urls'), name='waiter'),
    path(r'home/orders/', include('core.orders.dash.urls'), name='orders'),
] + urlpatterns_API + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
