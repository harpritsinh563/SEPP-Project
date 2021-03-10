from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Customer
from product_management.views import viewProducts
from product_management.models import Product, Category


def home(request):
    cart = request.session.get('cart')
    # When the homepage will be called for the first time.Session for the cart will be created
    if not cart:
        request.session['cart'] = {}
    return HttpResponse(viewProducts(request))


def login(request):
    if request.method == "POST":
        currentuser = authenticate(username=request.POST.get(
            'uname'), password=request.POST.get('pass'))
        if currentuser is not None:
            auth.login(request, currentuser)

            # Saving the user id and username into the current session so it can be accessed anywhere on the site and used for tracking the user
            request.session['currentuser'] = currentuser.id
            request.session['currentusername'] = currentuser.username
            return HttpResponseRedirect('/accounts/home')
        else:
            return render(request, 'invalidlogin.html')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    # When the user clicks signout,all the items in his session should be deleted
    request.session.clear()
    return HttpResponseRedirect('/accounts/home')


def signup(request):
    if request.method == "POST":
        # Confirm both entered passwords are matching
        if request.POST.get('pass') == request.POST.get('pass2'):
            try:
                user = User.objects.get(username=request.POST.get('uname'))
                # Two people cannot have same usernames
                return HttpResponse("User already exists")
            except User.DoesNotExist:
                uname = request.POST.get('uname')
                pwd = request.POST.get('pass')
                user = User.objects.create_user(username=uname, password=pwd, first_name=request.POST.get('fname'), last_name=request.POST.get(
                    'lname'), email=request.POST.get('email'))

                # Creating a customer object which extends the default user model of django and set additional fields other than
                # default fields of the django user table
                newCustomer = Customer()
                newCustomer.setAdditional(request.POST.get(
                    'phoneno'), request.POST.get('address'), user.id)
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
