from django.contrib import admin
from .models import Product, Review

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',        
        'price',        
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'product',
        'review',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Review)
