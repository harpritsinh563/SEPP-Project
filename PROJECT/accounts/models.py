from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneno = models.CharField(max_length=11)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

    def setAdditional(self, phoneno, address, id):
        self.phoneno = phoneno
        self.address = address
        self.user_id = id

    def addCustomer(self):
        self.save()

# For now :
# Accounts of supplier will be made from admin panel and id password will be given through some external communication
# Admin just sets a supply_order id in the supplier and when supplier logs in he will see that pending supply order
# Here supplier uses the website just to confirm the pending supply orders
# Supply orders will be given by management team(That has no relation with website)
# All these supplies of products will be held offline and has nothing to do with website
# Will be implementing more functionalities in later versions


class Supplier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    pending_order_id = models.CharField(max_length=10)
    pending_order_status = models.CharField(
        default='Pending', max_length=20)

    def __str__(self):
        return self.name
    # Means the supplier has to just confirm that supply order (Once supplies of products have been sent which will be offline)
    # Once the supplier confirms the supply order the pending_order_status is set to Supplied
