from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Product,Transactions
from .serializers import ProductSerializer,TransactionsSerializer,ShopSerializer
import requests
import pickle,json
import numpy as np
import tensorflow as tf
from MLModels.recommend import simulate_interactions

@api_view(['GET'])
def getProducts(request):
    data=Product.objects.all()
    serializer=ProductSerializer(data,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRecommendation(request,id):
    data=Product.objects.all()
    procSerializer=ProductSerializer(data,many=True)
    data=Transactions.objects.filter(customerId=id)
    transSerializer=TransactionsSerializer(data,many=True)
    past_transactions=[]
    for x in transSerializer.data:
        data_str = x['products'].replace("'", '"')
        data = json.loads(data_str)
        transaction_binary=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for i in data:
            index=int(i['id'])-1
            transaction_binary[int(index)]=1
        transactions_string = ''.join(str(v) for v in transaction_binary)
        past_transactions.append(transactions_string)
    output=simulate_interactions(past_transactions,id)
    result_list = [int(s.split('_')[1]) for s in output if s.split('_')[1].isdigit()]
    filtered_products = [product for product in procSerializer.data if product['productId'] in result_list]
    return Response(filtered_products)