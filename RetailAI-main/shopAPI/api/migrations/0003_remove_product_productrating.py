# Generated by Django 4.1.13 on 2023-11-04 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_product_productimageurl_product_productimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='productRating',
        ),
    ]
