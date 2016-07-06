__author__ = 'rj'

from django import  template
register = template.Library()

@register.filter
def rminus(item):
    try:
        return item.end - item.start
    except :
        return ''