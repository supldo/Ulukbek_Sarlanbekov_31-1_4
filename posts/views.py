from django.shortcuts import render, redirect

from posts.forms import CetagoryCreateForm, ProductCreateForm, ReviewCreateForm
from posts.models import Product, Category, Review


def main_view(request):
    if request.method == "GET":
        context_data = {
            'user': request.user,
        }
        return render(request, 'layouts/index.html', context=context_data)


def products_view(request):
    if request.method == "GET":
        products = Product.objects.all()
        context_data = {
            'products': products,
        }
        return render(request, 'products/products.html', context=context_data)


def categories_view(request):
    if request.method == "GET":
        category = Category.objects.all()
        context_data = {
            'category': category,
        }
        return render(request, 'products/categories.html', context=context_data)


def detail_view(request, id):
    if request.method == "GET":
        product = Product.objects.get(id=id)
        reviews = product.reviews.all()
        context_data = {
            'product': product,
            'reviews': reviews,
            'form': ReviewCreateForm,
        }
        return render(request, 'products/detail.html', context=context_data)
    if request.method == "POST":
        product = Product.objects.get(id=id)
        reviews = product.reviews.all()
        data = request.POST
        form = ReviewCreateForm(data)
        if form.is_valid():
            Review.objects.create(product=product, **form.cleaned_data)
            return redirect(f'/products/{id}')
        context_data = {
            'product': product,
            'reviews': reviews,
            'form': form,
        }
        return render(request, 'products/detail.html', context=context_data)


def create_categories_view(request):
    if request.user.is_anonymous:
        return redirect('/')
    if request.method == "GET":
        context_data = {
            'form': CetagoryCreateForm,
        }
        return render(request, 'products/create_categories.html', context=context_data)
    if request.method == "POST":
        data, files = request.POST, request.FILES
        form = CetagoryCreateForm(data, files)
        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect('/categories/')
        context_data = {
            'form': form
        }
        return render(request, 'products/create_categories.html', context=context_data)


def create_products_view(request):
    if request.user.is_anonymous:
        return redirect('/')
    if request.method == "GET":
        context_data = {
            'form': ProductCreateForm,
        }
        return render(request, 'products/create_products.html', context=context_data)
    if request.method == "POST":
        data, files = request.POST, request.FILES
        form = ProductCreateForm(data, files)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            return redirect('/products/')
        context_data = {
            'form': form
        }
        return render(request, 'products/create_products.html', context=context_data)
