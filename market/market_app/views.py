from django.shortcuts import render, get_object_or_404
from .models import Product
from django.core.mail import send_mail
from django.conf import settings
import random
import string


def main(request):
    if request.method == "POST":
        discout_code = "".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(10))
        message_email = request.POST['message-email']

        send_mail(message_email, f"Hello *name* it's your discount code '{discout_code}'", settings.EMAIL_HOST_USER, [message_email], fail_silently=False, )
        return render(request, "market_app/main.html")
    else:
        return render(request, "market_app/main.html")


def products(request):
    products = Product.objects.all()
    return render(request, "market_app/products.html", {"products": products})


def product_detail(request, id):
    product = Product.objects.filter(id=id)
    return render(request, "market_app/product_detail.html", {"product": product})