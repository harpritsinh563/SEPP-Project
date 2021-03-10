from django import template
register = template.Library()

# This filter just checks if the payment mode is offline or not


@register.filter(name='is_offline_payment')
def is_offline_payment(payment_type):
    if payment_type == "COD":
        return True
    else:
        False
