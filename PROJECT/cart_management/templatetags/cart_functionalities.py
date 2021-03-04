from django import template
register = template.Library()


@register.filter(name='show_quantity')
def show_quantity(product, cart):
    if cart:
        products_in_cart = cart.keys()
        for pid in products_in_cart:
            if pid is not None:
                if int(pid) == product.id:
                    return cart.get(pid)
        return -1


@register.filter(name='getProductsPrice')
def getProductsPrice(product, cart):
    totalprice = product.price * show_quantity(product, cart)
    return totalprice


@register.filter(name='getfinalamount')
def getfinalamount(products, cart):
    totalamount = 0
    for product in products:
        totalamount += getProductsPrice(product, cart)
    return totalamount


@register.filter(name='is_present_in_cart')
def is_present_in_cart(product, cart):
    if cart:
        products_in_cart = cart.keys()
        print(products_in_cart)
        for pid in products_in_cart:
            # print("pid :"+pid)
            if pid is not None:
                # print("pid inside if :"+pid)
                if int(pid) == product.id:
                    return True
    return False
