from django import template
register = template.Library()


@register.filter(name='isnotvalid')
def isnotvalid(promocode):
    if promocode == '-1':
        return True
    return False


@register.filter(name='isvalid')
def isvalid(promocode):
    if promocode:
        return True
    return False
