from django import forms
from .models import models, Category, Product


class CetagoryCreateForm(forms.Form):
    title = forms.CharField(max_length=32)
    icon = forms.FileField(required=False)


class ProductCreateForm(forms.Form):
    MEMORY_TYPE = [
        ('GDDR4', 'GDDR4'),
        ('GDDR5', 'GDDR5'),
        ('GDDR6', 'GDDR6'),
    ]
    image = forms.FileField(required=False)
    title = forms.CharField(max_length=128)
    brand = forms.CharField(max_length=32)
    memory = forms.IntegerField()
    memory_type = forms.ChoiceField(choices=MEMORY_TYPE)
    price = forms.IntegerField()


class ReviewCreateForm(forms.Form):
    rate = forms.FloatField()
    comment = forms.CharField(widget=forms.Textarea())