from django import template
register = template.Library()


# This filter is used for getting the quantity of each individual product added into the cart
@register.filter(name='show_quantity')
def show_quantity(product, cart):
    if cart:
        products_in_cart = cart.keys()
        for pid in products_in_cart:
            if pid is not None:
                if int(pid) == product.id:
                    return cart.get(pid)
        return -1

# This filter is used to get a particular products price


@register.filter(name='getProductsPrice')
def getProductsPrice(product, cart):
    totalprice = product.price * show_quantity(product, cart)
    return totalprice


# This filter is used to determine the final amount by summing up the quantity*price of all products in cart
@register.filter(name='getfinalamount')
def getfinalamount(products, cart):
    totalamount = 0
    for product in products:
        totalamount += getProductsPrice(product, cart)
    return totalamount


# This filter is used for checking if the product is present in cart or not
@register.filter(name='is_present_in_cart')
def is_present_in_cart(product, cart):
    if cart:
        products_in_cart = cart.keys()
        print(products_in_cart)
        for pid in products_in_cart:
            if pid is not None:
                if int(pid) == product.id:
                    return True
    return False


# This is tag which will be used to determine the discountedprice
# It accepts the promocode,products,cart
@register.simple_tag(name='getdiscountedprice')
def getdiscountedprice(a, *args, **kwargs):
    if a == '-1':
        return '-1'
    products = kwargs['products']
    cart = kwargs['cart']
    discountpercent = a.discount
    discount = getfinalamount(products, cart)*discountpercent/100
    return getfinalamount(products, cart)-discount


@register.filter(name="in_stock")
def in_stock(product):
    if product.inStock == True:
        return True
    return False
