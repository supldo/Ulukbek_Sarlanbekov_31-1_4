from django.shortcuts import render

from posts.models import Product
def main_view(request):
    if request.method == "GET":
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == "GET":
        products = Product.objects.all()

        context_data = {
            'products': products
        }

        return render(request, 'products/products.html', context=context_data)

