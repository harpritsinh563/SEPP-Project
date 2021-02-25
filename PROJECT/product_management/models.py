from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_name = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    brand = models.CharField(max_length=20, default='')
    inStock = models.BooleanField(default='True')
    description = models.CharField(max_length=255, default='')
    image = models.ImageField(upload_to='uploads/products/images/')

    def __str__(self):
        return self.product_name

    @staticmethod
    def getProducts():
        allproducts = Product.objects.all()
        return allproducts
