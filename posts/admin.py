from django.contrib import admin

from posts.models import Product, Category

admin.site.register(Product)
admin.site.register(Category)
