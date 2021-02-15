from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path
from loginmodule.views import login, auth_view, logout, loggedin, invalidlogin
urlpatterns = [
    url('login/', login),
    url('auth/', auth_view),
    url('logout/', logout),
    url('loggedin/', loggedin),
    url('invalidlogin/', invalidlogin),
]
