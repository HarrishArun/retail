from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import UserSerializer,LoginSerializer,TransactionSerializer,ProductsInTransactionSerializer
from .models import User
from rest_framework import status
import json
@api_view(['GET'])
def getAllUsers(request):
    data=User.objects.all()
    serializer=UserSerializer(data,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUser(request,id):
    try:
        user = User.objects.get(id=id)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def addUser(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user_data = serializer.validated_data
        user = User.objects.create(
            name=user_data['name'],
            email=user_data['email'],
            phoneNumber=user_data['phoneNumber']
        )
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=400)

@api_view(['GET','POST'])
def addTransation(request,id):
    serializer=TransactionSerializer(data=request.data)
    if serializer.is_valid():
        user_data=serializer.validated_data
        user=User.objects.get(id=id)
        user_transactions=user.transactions
        new_transaction={
            "id":user_data['id'],
            "shop_id":user_data['shop_id'],
            "products":user_data['products']
        }
        procSerializer=ProductsInTransactionSerializer(user_data['products'])
        if procSerializer.is_valid:
            user_transactions.append(new_transaction)
            user.transactions=user_transactions
            user.save()
            return Response({'message':'Operation done and data updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(procSerializer.errors,status=400)
    else:
        return Response(serializer.errors, status=400)