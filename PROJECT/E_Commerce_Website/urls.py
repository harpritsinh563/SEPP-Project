"""E_Commerce_Website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls.static import static
from accounts.views import home
from accounts import urls
from . import settings
from product_management import urls
from cart_management import urls
from orderhandling import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('accounts/', include('accounts.urls')),
    path('product_management/', include('product_management.urls')),
    path('cart_management/', include('cart_management.urls')),
    path('promocodes/', include('promocodes.urls')),
    path('orderhandling/', include('orderhandling.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
