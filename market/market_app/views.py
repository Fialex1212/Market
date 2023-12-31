from django.shortcuts import render, get_object_or_404
from .models import Product


def main(request):
    return render(request, "market_app/main.html")

def product_detail(request, id):
    obj = Product.objects.filter(id=id)
    return render(request, "market_app/product_detail.html", {'obj': obj})