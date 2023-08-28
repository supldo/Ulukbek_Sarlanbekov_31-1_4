from django.contrib import admin

from posts.models import Product, Category, Review


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
    'title', 'brand', 'memory', 'memory_type', 'price', 'rate', 'discount', 'created_date', 'modified_date')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'product')
