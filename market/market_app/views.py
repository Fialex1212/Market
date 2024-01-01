from django.shortcuts import render, get_object_or_404
from .models import Product


def main(request):
    return render(request, "market_app/main.html")


def products(request):
    products = Product.objects.all()
    return render(request, "market_app/products.html", {"products": products})


def product_detail(request, id):
    product = Product.objects.filter(id=id)
    return render(request, "market_app/product_detail.html", {"product": product})