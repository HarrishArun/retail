# Generated by Django 4.1.13 on 2023-11-04 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_product_productrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productImage',
            field=models.ImageField(default='shopAPI\\media\\pics\\default-product-image.png', upload_to='pics'),
        ),
    ]
