from django.shortcuts import render
from .models import Product, Category
# Create your views here.


def viewProducts(request):
    categories = Category.getCategories()
    # If the customer clicks on a specific category he will be served with all the products of that category
    # Else all the products will be served
    if request.GET.get('categoryid'):
        products = Product.get_specific_category_products(
            request.GET.get('categoryid'))
    else:
        products = Product.getProducts()
    return render(request, 'homepage.html', {'products': products, 'categories': categories})


def getcategories(request):
    categories = Category.getCategories()
    return render(request, 'base.html', {'categories': categories})


def show_product_details(request):
    productid = request.GET.get('productid')
    product = Product.objects.get(id=productid)
    return render(request, 'productdetails.html', {'product': product})
