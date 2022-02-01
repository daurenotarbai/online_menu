from django import template

register = template.Library()

@register.filter
def str_replace(value):
    return value.replace(" ","")