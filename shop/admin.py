from django.contrib import admin
from shop.models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description", "category", "remainder", "cost"]
    list_filter = ["id", "name", "category"]
    search_fields = ["id", "name", "category"]
    fields = ["id", "name", "category", "description", "remainder", "cost"]
    readonly_fields = ["id"]

admin.site.register(Product, ProductAdmin)