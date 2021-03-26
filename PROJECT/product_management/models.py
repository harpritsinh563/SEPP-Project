from django.db import models
from accounts.models import Customer
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    @staticmethod
    def getCategories():
        allcategories = Category.objects.all()
        return allcategories


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

    @staticmethod
    def get_specific_category_products(categoryid):
        if categoryid:
            category_products = Product.objects.filter(category_id=categoryid)
            return category_products
        else:
            return getProducts()


class Review(models.Model):
    review = models.CharField(max_length=255)
    given_by = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
