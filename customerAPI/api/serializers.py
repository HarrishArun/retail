from rest_framework import serializers
from .models import User  # Import your model if needed
from jsonfield import JSONField

class UserSerializer(serializers.ModelSerializer): #userSerializer
    class Meta:
        model = User  # Set the model for the serializer
        fields = '__all__'  # Include all model fields

class LoginSerializer(serializers.Serializer): #loginSerializer
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phoneNumber = serializers.CharField(max_length=10)

class TransactionSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    shop_id=serializers.IntegerField()
    products=serializers.JSONField()
    
class ProductsInTransactionSerializer(serializers.Serializer):
    id=serializers.IntegerField(required=True)
    product_name=serializers.CharField(required=True)
    product_qty=serializers.IntegerField(required=True)
    product_price=serializers.DecimalField(max_digits=10,decimal_places=2,required=True)