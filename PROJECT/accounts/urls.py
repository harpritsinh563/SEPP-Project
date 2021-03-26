from django.urls import path
from .views import signup, login, logout, home, updateinfo, supplierlogin, dashboard, supply_confirm

urlpatterns = [
    path('home/', home, name="homepage"),
    path('signup', signup, name="signup"),
    path('login', login, name="login"),
    path('logout', logout, name="logout"),
    path('updateinfo', updateinfo, name="update"),
    path('supplierlogin', supplierlogin, name="supplier"),
    path('supplierdashboard', dashboard, name="supplierdashboard"),
    path('confirmsupplies', supply_confirm, name="confirmsupplies")
]
