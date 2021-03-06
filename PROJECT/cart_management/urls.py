from django.urls import path
from .views import add_to_cart, remove_from_cart,viewCart,checkout
urlpatterns = [
    path('add_to_cart', add_to_cart, name="add_to_cart"),
    path('remove_from_cart', remove_from_cart, name="remove_from_cart"),
    path('viewCart',viewCart,name="viewCart"),
    path('checkout',checkout,name="checkout"),
]
