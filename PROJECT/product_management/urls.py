
# Urls of Product application
from django.urls import path
from accounts.views import home
from .views import viewProducts
urlpatterns = [
    path('home', home),
    path('viewproducts',viewProducts),
]
