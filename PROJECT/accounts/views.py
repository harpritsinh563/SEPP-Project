from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Customer
from product_management.models import Product


def home(request):
    products = Product.getProducts()
    return render(request, 'homepage.html', {'products': products})


def login(request):
    if request.method == "POST":
        currentuser = authenticate(username=request.POST.get(
            'uname'), password=request.POST.get('pass'))
        if currentuser is not None:
            auth.login(request, currentuser)
            return render(request, 'loggedin.html')
        else:
            return render(request, 'invalidlogin.html')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'loggedout.html')


def signup(request):
    if request.method == "POST":
        postData = request.POST

        # Confirm both passwords are matching
        if postData.get('pass') == postData.get('pass2'):
            try:
                user = User.objects.get(username=postData.get('uname'))
                return HttpResponse("User already exists")
            except User.DoesNotExist:
                uname = postData.get('uname')
                pwd = postData.get('pass')
                user = User.objects.create_user(username=uname, password=pwd, first_name=postData.get('fname'), last_name=postData.get(
                    'lname'), email=postData.get('email'))
                newCustomer = Customer()
                newCustomer.setAdditional(postData.get(
                    'phoneno'), postData.get('address'), user.id)
                auth.login(request, user)
                user.save()
                newCustomer.addCustomer()
                return HttpResponse("Thank you for signing up")
        else:
            return HttpResponse("Passwords do not match")
    else:
        return render(request, 'signup.html')


def updateinfo(request):
    if request.method == "POST":
        postData = request.POST
        user = authenticate(username=request.user.username,
                            password=request.POST.get('pass'))
        updatedCustomer = Customer.objects.get(
            user_id=user.id)
        updatedCustomer.phoneno = request.POST.get('nphone')
        updatedCustomer.address = request.POST.get('naddress')
        user.email = request.POST.get('nemail')
        updatedCustomer.save()
        user.save()
        return render(request, 'loggedin.html', {'confirm': "Successfully updated"})
    else:
        current_user = request.user
        current_customer = Customer.objects.get(user_id=current_user.id)
        return render(request, 'update.html', {'customer': current_customer})


# def getCurrentUser(request):

    # @login_required(login_url='/login/')
    # def ViewLoggedInUser(request):
    #     users_data = Customer.objects.filter(username=request.username)
    #     return render(request, 'showuser.html', {'data': users_data})
