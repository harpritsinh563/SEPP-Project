from django import template
register = template.Library()


@register.filter(name='pending')
def pending(orderstatus):
    if orderstatus == "Pending":
        return True
    return False
