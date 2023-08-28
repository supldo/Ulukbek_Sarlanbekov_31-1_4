from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=32)
    icon = models.ImageField(upload_to='images/category_icon/', blank=True, null=True)


class Product(models.Model):
    MEMORY_TYPE = [
        ('GDDR4', 'GDDR4'),
        ('GDDR5', 'GDDR5'),
        ('GDDR6', 'GDDR6'),
    ]
    image = models.ImageField(upload_to='images/product_image/', blank=True, null=True)
    title = models.CharField(max_length=128)
    brand = models.CharField(max_length=32)
    memory = models.IntegerField()
    memory_type = models.CharField(max_length=16, choices=MEMORY_TYPE)
    price = models.IntegerField()
    rate = models.FloatField(default=0)
    discount = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name="categories")


class Review(models.Model):
    rate = models.FloatField(default=0)
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
