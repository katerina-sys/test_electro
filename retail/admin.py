from django.contrib import admin

# Register your models here.

from retail.models import Retail, Contractor, Seller


class RetailAdmin(admin.ModelAdmin):
    list_display = ("title", "country", "city", "email")
    search_fields = ("title", "city")
    list_filter = "city"


class ContractorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "retail_id")
    search_fields = ("first_name", "last_name", "retail_id")


class SellerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "retail_id")
    search_fields = ("first_name", "last_name", "retail_id")


admin.site.register(Contractor)
admin.site.register(Retail)
admin.site.register(Seller)
