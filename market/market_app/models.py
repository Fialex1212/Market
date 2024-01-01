from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, default="Unknown Brand")
    img = models.ImageField(upload_to='market_app/product_images/', default="market_app/default.png")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)#on_delete means that if a category is deleted, all associated items will also be deleted.
    type = models.CharField(max_length=255, default="Unknown Type")
    color = models.CharField(max_length=600)
    sex = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

