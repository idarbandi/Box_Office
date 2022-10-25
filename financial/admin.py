from django.contrib import admin
from django.contrib.admin import register

from financial.models import Gateway, Payment


@register(Gateway)
class GatewayAdmin(admin.ModelAdmin):
    list_display = ['title', 'gateway_code', 'is_enable',
                    'created_time', ]


# class GatewayStack(admin.StackedInline):
#     model = Gateway


@register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    search_fields = ['amount', 'user']
    list_display = ['invoice_number', 'amount', 'gateway', 'is_paid',
                    'payment_log', 'user', 'authority', ]
    list_filter = ['payment_log']
    # inlines = [GatewayStack]
