from django import template
register = template.Library()

# Filter used to check if the promocode is not valid for template
# In the view part I have sent promocode = -1 so to just check what to display in the template


@register.filter(name='isnotvalid')
def isnotvalid(promocode):
    if promocode == '-1':
        return True
    return False

# In the view part I have sent valid promocode so to just check what to display in the promocode.html template


@register.filter(name='isvalid')
def isvalid(promocode):
    if promocode:
        return True
    return False
