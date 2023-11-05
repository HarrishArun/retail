from django.contrib import admin
from .models import Product,Shop,Transactions
# Register your models here.
class imageAdmin(admin.ModelAdmin):
    list_display = ["productName", "productImage"]
admin.site.register(Product,imageAdmin)
admin.site.register(Shop)
admin.site.register(Transactions)