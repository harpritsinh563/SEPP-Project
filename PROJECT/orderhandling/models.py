from django.db import models
from accounts.models import Customer
from datetime import datetime, timedelta
# Create your models here.


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_created = models.DateTimeField(default=datetime.today())
    totalamount = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=255)
    phoneno1 = models.CharField(max_length=10)
    phoneno2 = models.CharField(max_length=10)
    expected_delivery = models.DateTimeField(
        default=datetime.today()+timedelta(6))
    payment_type = models.CharField(max_length=20)
