from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializers
from rest_framework import status
# Create your views here.

@api_view(["GET","POST"])
def Product_list(request):
    if request.method == 'GET':
        obj = Product.objects.all()
        serializers = ProductSerializers(obj,many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = ProductSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT"])
def Single_Product(request,prodId):
    try:
        obj = Product.objects.get(id=prodId)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer= ProductSerializers(obj)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializers = ProductSerializers(obj,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializers.errors,status=status.HTTP_404_NOT_FOUND)