from django.contrib import admin
from transactions.models import *
from django.contrib.admin import register


@register(transaction)
class TransAdmin(admin.ModelAdmin):
    list_display = ['user', 'type', 'amount', 'updateDate']
    search_fields = ['user__username']
    list_filter = ['type']


@register(UserBalance)
class BalanceUserAdmin(admin.ModelAdmin):
    list_display = ['user']
    search_fields = ['user']
