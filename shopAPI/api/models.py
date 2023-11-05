from django.db import models
from django.utils import timezone
from jsonfield import JSONField
import tensorflow as tf
import numpy as np
class Shop(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,blank=False,default="")
    gstin = models.CharField(max_length=255,blank=False,default="")
    area = models.CharField(max_length=255,blank=False,default="")
    address = models.CharField(max_length=255,default="")
    phoneNumber = models.CharField(max_length=255,default="")
    def __str__(self):
        return str(self.id)
    
class Transactions(models.Model):
    id=models.AutoField(primary_key=True)
    shopId=models.ForeignKey(Shop, on_delete=models.CASCADE,unique=False)
    customerId=models.IntegerField(blank=False,default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    products=JSONField(default=[])

    def __str__(self):
        return str(self.id)
    
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    shopId = models.ForeignKey(Shop, on_delete=models.CASCADE)
    productId = models.IntegerField(unique=False,blank=False,default=0)
    productName = models.CharField(max_length=255,blank=False,default="")
    productImage = models.ImageField(upload_to='pics',default='shopAPI\media\pics\default-product-image.png')
    productQty=models.CharField(max_length=255,blank=False,default="")
    productDescription = models.TextField(default="")
    productCostPrice = models.DecimalField(max_digits=10, decimal_places=2,blank=False,default=0)
    productSellingPrice = models.DecimalField(max_digits=10, decimal_places=2,blank=False,default=0)
    productDiscountPercentage = models.DecimalField(max_digits=5, decimal_places=2,default=0.0)

    class Meta:
        unique_together = [['shopId', 'productId']]

    def __str__(self):
        return str(self.id)
    
