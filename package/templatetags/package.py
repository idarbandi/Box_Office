from package.models import Package
from django import template

register = template.Library()


@register.simple_tag
def PackInit():
    return Package.objects.exclude(is_golden=True)


@register.simple_tag
def golden():
    return Package.objects.filter(is_golden=True)
