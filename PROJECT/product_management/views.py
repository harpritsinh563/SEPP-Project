from django.shortcuts import render
from .models import Product, Category, Review
from django.http import HttpResponse, HttpResponseRedirect
from accounts.models import Customer
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
    reviews = Review.objects.filter(product_id=productid)
    return render(request, 'productdetails.html', {'product': product, 'reviews': reviews})


def search(request):
    product_query = request.GET.get('search')
    products = Product.getProducts()
    matching_products = []
    for p in products:
        if product_query.casefold() in p.product_name.casefold() or product_query.casefold() in p.category.name.casefold() or product_query in p.description.casefold():
            matching_products.append(p)
    print('Matching products : '+str(matching_products))
    if len(matching_products) != 0:
        return render(request, 'homepage.html', {'products': matching_products,'matchingfound':True})
    else:
        return render(request, 'homepage.html', {'productnotfound': True})


def addreview(request):
    if request.method == "POST":
        ip_review = request.POST.get('review')
        ip_rating = request.POST.get('rating')
        ip_product = request.POST.get('product')
        print('ip review '+str(ip_review)+'\nip_rating' +
              str(ip_rating)+'\nproduct '+str(ip_product))
        c_user = request.user
        print('c_user'+str(c_user))
        product = Product.objects.get(product_name=ip_product)
        customer = Customer.objects.get(user_id=c_user.id)
        review = Review(review=ip_review, rating=ip_rating,
                        given_by=customer, product=product)
        review.save()
        reviews = Review.objects.filter(product_id=product.id)
        return render(request, 'productdetails.html', {'product': product, 'reviews': reviews})
