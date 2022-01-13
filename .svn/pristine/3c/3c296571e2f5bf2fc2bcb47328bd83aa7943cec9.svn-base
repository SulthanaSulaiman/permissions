import datetime
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)

@register.simple_tag

def store_list(items):
    itarray = []
    for items in itarray:
        if items not in itarray:
            itarray.append(items)
            return itarray


def main():
    global itarray