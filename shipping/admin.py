from django.contrib import admin
from django.contrib.admin import register

from shipping.models import shipping


@register(shipping)
class ShippingAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'zipcode']