from django.contrib import admin

# Register your models here.

from factory.models import Products, Factory


class ProductsAdmin(admin.ModelAdmin):
    list_display = ("title", "model", "created", "price")
    search_fields = ("title", "model", "created")


class FactoryAdmin(admin.ModelAdmin):
    list_display = ("title", "country", "email", "city")
    search_fields = ("title", "country", "city")
    list_filter = "city"


admin.site.register(Products)
admin.site.register(Factory)
