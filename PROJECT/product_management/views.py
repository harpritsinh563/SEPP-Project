from django.shortcuts import render
from .models import Product, Category
# Create your views here.


def viewProducts(request):
    categories = Category.getCategories()
    print(request.GET.get('categoryid'))
    if request.GET.get('categoryid'):
        products = Product.get_specific_category_products(
            request.GET.get('categoryid'))
    else:
        products = Product.getProducts()
    return render(request, 'homepage.html', {'products': products, 'categories': categories})


def show_product_details(request):
    productid = request.GET.get('productid')
    product = Product.objects.get(id=productid)
    return render(request, 'productdetails.html', {'product': product})
