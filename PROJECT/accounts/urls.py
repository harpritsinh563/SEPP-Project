from django.urls import path
from .views import signup, login, logout, home

urlpatterns = [
    path('home', home, name="homepage"),
    path('signup', signup, name="signup"),
    path('login', login, name="login"),
    path('logout', logout, name="logout"),
    
]
