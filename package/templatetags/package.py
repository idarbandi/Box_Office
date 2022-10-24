from package.models import Package
from django import template

register = template.Library()


@register.simple_tag
def PackInit():
    return Package.objects.exclude(price=75000)


@register.simple_tag
def golden():
    return Package.objects.filter(price=75000)
