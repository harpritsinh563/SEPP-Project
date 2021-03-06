from django.db import models

# Create your models here.


class Promocode(models.Model):
    code = models.CharField(max_length=6)
    discount = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    @staticmethod
    def getactivepromocodes():
        return Promocode.objects.filter(active=True)

    def __str__(self):
        return self.code
