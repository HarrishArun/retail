# Generated by Django 4.1.13 on 2023-11-04 12:42

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=255)),
                ('gstin', models.CharField(default='', max_length=255)),
                ('area', models.CharField(default='', max_length=255)),
                ('address', models.CharField(default='', max_length=255)),
                ('phoneNumber', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('customerId', models.IntegerField(default=0)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('products', jsonfield.fields.JSONField(default=[])),
                ('shopId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.shop')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('productId', models.IntegerField(default=0)),
                ('productName', models.CharField(default='', max_length=255)),
                ('productImageUrl', models.CharField(default='', max_length=255)),
                ('productRating', jsonfield.fields.JSONField(default=[])),
                ('productQty', models.CharField(default='', max_length=255)),
                ('productDescription', models.TextField(default='')),
                ('productCostPrice', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('productDiscountPercentage', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('shopId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.shop')),
            ],
            options={
                'unique_together': {('shopId', 'productId')},
            },
        ),
    ]