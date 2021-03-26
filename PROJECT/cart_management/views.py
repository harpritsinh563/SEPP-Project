from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from product_management.models import Product
# Create your views here.

# Cart is managed completely with session.
# All additions,deletions,updations in cart are carried out through sessions only


def checkout(request):
    loggedin = request.session.get('currentuser')
    # This is to check if the user is logged in
    # User cannot checkout the items without logging in
    if loggedin:
        return HttpResponseRedirect('/promocodes/getpromocode')
    else:
        return render(request, 'login.html', {'loginrequired': True})


def add_to_cart(request):
    productid = request.POST.get('productid')  # selected product
    cart = request.session.get('cart')
    if cart:
        quantity = cart.get(productid)
        if quantity:
            cart[productid] += 1
        else:
            cart[productid] = 1
    else:
        cart = {}
        cart[productid] = 1
    request.session['cart'] = cart
    return HttpResponseRedirect('/product_management/viewproducts')


def remove_from_cart(request):
    productid = request.POST.get('productid')  # selected product
    cart = request.session.get('cart')
    if cart:
        quantity = cart.get(productid)
        if quantity == 1:
            cart.pop(productid)
        else:
            cart[productid] -= 1
    request.session['cart'] = cart
    return HttpResponseRedirect('/product_management/viewproducts')


def viewCart(request):
    cart = request.session.get('cart')
    products_in_cart = list(cart.keys())
    # print(products_in_cart)
    product_objs = Product.objects.filter(id__in=products_in_cart)
    return render(request, 'cart.html', {'cart': product_objs})
