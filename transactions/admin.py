from django.contrib import admin
from transactions.models import *
from django.contrib.admin import register


@register(transaction)
class TransAdmin(admin.ModelAdmin):
    list_display = ['user', 'type', 'amount', 'updateDate']
    search_fields = ['user']


@register(UserBalance)
class BalanceUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'balance']
    search_fields = ['user']
