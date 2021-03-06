from django.urls import path
from .views import validatePC,promocodepage
urlpatterns = [
    path('validatepromocode', validatePC, name="validatepromocode"),
    path('getpromocode', promocodepage, name="getpromocode"),

]
