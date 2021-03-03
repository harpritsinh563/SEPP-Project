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
