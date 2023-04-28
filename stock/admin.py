from django.contrib import admin

from .models import Stock
from product.models import Product

class ProductInline(admin.TabularInline):
    model = Product
    extra = 3

class StockAdmin(admin.ModelAdmin):
    list_display = (
                    'name',
                    'slug',
                    'user',
                    )
    search_fields = (
                    'name',
                    'slug',
                    'user__username',
                    )
    ordering = (
                'user__username', 
                'name',
                'slug',
                )
    list_filter = (
                    'user__username',
                    'name',
                    'slug',
                    )
    inlines = (
                ProductInline,
                )

# Register your models here.
admin.site.register(Stock, StockAdmin)