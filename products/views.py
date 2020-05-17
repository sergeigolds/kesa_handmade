from django.shortcuts import render
from django.views.generic.base import View

from .models import Product


class ProductsView(View):
    """Products list"""
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'products/products_page.html', {'products_list': products})


class ProductDetailView(View):
    """Products list"""
    def get(self, request, slug):
        product = Product.objects.get(url=slug)
        return render(request, 'products/single_product_details.html', {'product': product})
