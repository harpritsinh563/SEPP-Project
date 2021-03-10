from django.urls import path
from .views import serveorderform, placeorder, completepayment
urlpatterns = [
    path('orderform', serveorderform, name="orderform"),
    path('placeorder', placeorder, name="placeorder"),
    path('completepayment', completepayment, name="completepayment"),
]
