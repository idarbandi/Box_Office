from django.contrib import admin
from django.contrib.admin import register

from distributer.models import *


class DistInline(admin.TabularInline):
    model = MovieDistributer


@register(Distributer)
class DistAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_filter = ['name']
    search_fields = ['name']
    inlines = [DistInline]
