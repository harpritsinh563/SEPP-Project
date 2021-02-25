from django.shortcuts import render
from .models import Product, Category
# Create your views here.


def viewProducts(request):
    products = Product.getProducts()
    return render(request, 'products.html', {'products': products})
