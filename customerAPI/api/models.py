from django.db import models
from jsonfield import JSONField
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True,default="")
    password=models.CharField(max_length=255,default="")
    phoneNumber = models.CharField(max_length=255)
    wishlist = JSONField(default=[{}])
    transactions = JSONField(default=[{}])
    shops_saved=JSONField(default=[{}])
    def __str__(self):
        return self.name

    def get_wishlist(self):
        return self.wishlist or []

    def set_wishlist(self, wishlist):
        self.wishlist = wishlist

    def get_transactions(self):
        return self.transactions or []

    def set_transactions(self, transactions):
        self.transactions = transactions
