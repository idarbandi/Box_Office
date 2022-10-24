from django.contrib import admin
from django.contrib.admin import register

from package.models import Package, Benefits


class Description(admin.TabularInline):
    model = Benefits


@register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'is_enable', 'description', 'days']
    search_fields = ['title']
    inlines = [Description]
