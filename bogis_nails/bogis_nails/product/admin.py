from django.contrib import admin

from bogis_nails.product.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at')
    list_filter = ('title', 'price', 'created_at', 'modified_at')
    search_fields = ('title', 'price', 'created_at', 'modified_at')
    
    