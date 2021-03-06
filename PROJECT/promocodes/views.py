from django.shortcuts import render
from .models import Promocode
from product_management.models import Product
from django.http import HttpResponse
from cart_management.views import viewCart
# Create your views here.


def promocodepage(request):
    cart = request.session.get('cart')
    products_in_cart = list(cart.keys())
    product_objs = Product.objects.filter(id__in=products_in_cart)
    return render(request, 'promocode.html', {'cart': product_objs, 'validpc': ''})


def validatePC(request):
    if request.method == "POST":
        promocode = request.POST.get('promocode')
        activepromocodes = list(Promocode.getactivepromocodes())
        cart = request.session.get('cart')
        products_in_cart = list(cart.keys())
        product_objs = Product.objects.filter(id__in=products_in_cart)
        valid = None
        for pc in activepromocodes:
            if promocode == pc.code:
                valid = pc
                break
        if valid is not None:
            return render(request, 'promocode.html', {'validpc': valid, 'cart': product_objs})
        else:
            return render(request, 'promocode.html', {'error': 'Invalid Promo Code', 'cart': product_objs, 'validpc': '-1'})
