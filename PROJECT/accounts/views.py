from django.shortcuts import render
from .models import Customer
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'homepage.html')


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
                user = User.objects.create_user(username=uname, password=pwd)
                newCustomer = Customer(firstname=postData.get('fname'), lastname=postData.get(
                    'lname'), email=postData.get('email'), phoneno=postData.get('phoneno'), username=uname, password=pwd)
                newCustomer.addCustomer()
                auth.login(request, user)
                return HttpResponse("Thank you for signing up")
        else:
            # render(request, 'signup.html', {'error': "Entered passwords do not match"})
            return HttpResponse("Passwords do not match")
    else:
        return render(request, 'signup.html')


# @login_required(login_url='/login/')
# def ViewLoggedInUser(request):
#     users_data = Customer.objects.filter(username=request.username)
#     return render(request, 'showuser.html', {'data': users_data})
