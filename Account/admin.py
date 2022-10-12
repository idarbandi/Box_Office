from django.contrib import admin
from django.contrib.admin import register
from Account.models import Account, BasketLines


@register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_time']




@register(BasketLines)
class BasketAdmin(admin.ModelAdmin):
    list_display = ['account', 'movie', 'quantity']
