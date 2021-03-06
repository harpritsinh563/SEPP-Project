
# Urls of Product application
from django.urls import path
from accounts.views import home
from .views import viewProducts, show_product_details, getcategories, addreview,search
urlpatterns = [
    path('home', home, name="home"),
    path('viewproducts', viewProducts, name="viewproducts"),
    path('show_product_details/', show_product_details,
         name="show_product_details"),
    path('getcategories', getcategories, name="getcategories"),
    path('addreview', addreview, name="addreview"),
    path('searchproduct',search, name="searchproduct")
]
