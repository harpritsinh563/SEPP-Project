from django.db import models

# Create your models here.


class Customer(models.Model):
    username = models.CharField(max_length=16)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    phoneno = models.CharField(max_length=10)
    password = models.CharField(max_length=16)

    def addCustomer(self):
        self.save()
