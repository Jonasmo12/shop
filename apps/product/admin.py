from django.contrib import admin
from .models import Product, Tag


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'shop', 'slug', 'price',
                    'in_stock', 'created_date']
    list_filter = ['in_stock', 'created_date']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass