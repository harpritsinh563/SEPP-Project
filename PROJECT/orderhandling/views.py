from django.shortcuts import render
from django.http import HttpResponse
from .models import Order
from accounts.models import Customer
# Create your views here.


def serveorderform(request):
    # To get the hidden field which is sent through button
    finalamount = request.POST.get('finalamount')
    return render(request, 'orderform.html', {'finalamount': finalamount})


def placeorder(request):
    address = request.POST.get('daddress')
    phoneno1 = request.POST.get('phone1')
    phoneno2 = request.POST.get('phone2')
    finalamount = request.POST.get('finalamount')
    payment_type = request.POST.get('payment_type')
    # Will fetch the customer who is logged in currently from the Customer Table
    customer = Customer.objects.get(user_id=request.session.get('currentuser'))
    order = Order(customer=customer, totalamount=finalamount, address=address,
                  phoneno1=phoneno1, phoneno2=phoneno2, payment_type=payment_type)
    order.save()
    # If the customer places the order then,current cart's session will be removed
    del request.session['cart']
    return render(request, 'orderdetails.html', {'order': order})


def completepayment(request):
    # For now I have kept that if customer selects an online payment method just show payment successful
    # Will integrate payment gateway later on
    return render(request, 'paymentstatus.html')
