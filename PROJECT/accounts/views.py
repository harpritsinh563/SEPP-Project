from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Customer, Supplier
from product_management.views import viewProducts
from product_management.models import Product, Category
import re


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
        errors = []
        # Confirm both entered passwords are matching
        if request.POST.get('pass') == request.POST.get('pass2'):
            try:
                user = User.objects.get(username=request.POST.get('uname'))
                # Two people cannot have same usernames
                already_exist = "User with that username already exists"
                errors += [already_exist]
                return render(request, 'signup.html', {'errors': errors, 'errorpresent': True})
            except User.DoesNotExist:
                uname = request.POST.get('uname')
                pwd = request.POST.get('pass')
                # Validating password criteria

                # Validating length criteria
                if len(pwd) < 8:
                    length_error = "Password must be 8 characters in length"
                    errors += [length_error]
                # Validating digit criteria
                contains_digit = bool(re.search(r'\d', pwd))
                if contains_digit == False:
                    digit_error = "Password must contain atleast 1 digit"
                    errors += [digit_error]
                # Validating alphabets
                contains_alphabets = bool(re.match('[a-zA-Z\s]+$', pwd))
                if contains_alphabets == "False":
                    alpha_error = "Password must contain atleast 1 alphabet"
                    errors += [alpha_error]
                # Validating special characters
                regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
                contains_special = bool(regex.search(pwd))
                if contains_special == False:
                    specialchar_error = "Password must contain atleast 1 special character"
                    errors += [specialchar_error]
                print(errors)
                if len(errors) >= 1:
                    return render(request, 'signup.html', {'errors': errors, 'errorpresent': True})
                else:
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
                    request.session['currentuser'] = user.id
                    request.session['currentusername'] = user.username
                    return HttpResponseRedirect('/accounts/home')
        else:
            pnm="Both entered passwords do not match"
            errors+=[pnm]
            return render(request, 'signup.html', {'errors':errors,'errorpresent':True})
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

# Following views are for supplier

# For now :
# Admin will manually add the supplier from login panel
# username and password (Login credentials) will be provided to supplier through some external offline communication
# Offline management team(Nothing to do with website) will generate an supply_order id which will be set into the suppliers pending order id column through admin only
# Supplier has to just confirm that supply order once he confirms the supply order (After sending all the supplies) the pending_order_status will be set to "Supplied"
# Will add more functionalities in future releases


def supplierlogin(request):
    if request.method == "POST":
        currentuser = authenticate(username=request.POST.get(
            'uname'), password=request.POST.get('pass'))
        if currentuser is not None:
            auth.login(request, currentuser)
            # Saving the user id and username into the current session so it can be accessed anywhere on the site and used for tracking the user
            request.session['currentuser'] = currentuser.id
            request.session['currentusername'] = currentuser.username
            return HttpResponseRedirect('/accounts/supplierdashboard')
    else:
        return render(request, 'login.html', {'supplier': True})


def dashboard(request):
    supplier = Supplier.objects.get(user_id=request.user)
    return render(request, 'supplier.html', {'supplierinfo': supplier})


def supply_confirm(request):
    supplier = Supplier.objects.get(user_id=request.user)
    supplier.pending_order_status = "Supplied"
    supplier.save()
    return HttpResponseRedirect('/accounts/supplierdashboard')
