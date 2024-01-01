from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name="main"),
    path('products', views.products, name="products"),
    path('product_detail/<int:id>', views.product_detail, name="product_detail")
]