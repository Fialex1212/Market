# Generated by Django 5.0 on 2023-12-30 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market_app', '0002_category_product_img_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(default='default.png', upload_to='product_images/'),
        ),
    ]