from django.db import models

class Product(models.Model):
    MEMORY_TYPE = [
        ('GDDR4','GDDR4'),
        ('GDDR5','GDDR5'),
        ('GDDR6','GDDR6'),
    ]

    image = models.ImageField(upload_to='product_image', blank=True, null=True)
    title = models.CharField(max_length=128)
    brand = models.CharField(max_length=32)
    memory = models.IntegerField()
    memory_type = models.CharField(max_length=16, choices=MEMORY_TYPE)
    price = models.IntegerField()
    rate = models.FloatField(default=0)
    discount = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(auto_now_add=True)

