from app import models
from . import serializers
from rest_framework . decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import generics

#class based view

class MakeOrder(generics.ListCreateAPIView):
    queryset = models.MakeOrder.objects.all()
    serializer_class = serializers.MakeOrderSerializer

class Delivery(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
    queryset = models.DeliveryOrder.objects.all()
    serializer_class = serializers.DeliveryOrderSerializer

#list of all reviews
class ReviwsList(generics.ListCreateAPIView):
    queryset=models.Review.objects.all()
    serializer_class= serializers.ReviewSerializer

#single review update delete.
class ReviewUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

# function based get, post, put 


# @api_view(['GET','POST'])
# def makeOrder(request):
#     if request.method =='GET':
#         orders = models.MakeOrder.objects.all()
#         serializer = serializers.MakeOrderSerializer(orders,many=True)
        
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = serializers.MakeOrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
    



# @api_view(['GET','POST'])
# def delivery(request):
#     if request.method == 'GET':
#         model = models.DeliveryOrder.objects.all()
#         serializer = serializers.DeliveryOrderSerializer(model,many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = serializers.DeliveryOrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','PATCH','DELETE','POST'])
# def details(request, pk):
#     order = get_object_or_404(models.MakeOrder, pk=pk)
#     if request.method == 'GET':
#         serializer = serializers.MakeOrderSerializer(order)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = serializers.MakeOrderSerializer(order,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'PUT':
#         serializer = serializers.MakeOrderSerializer(order,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
#     elif request.method == 'PATCH':
#         serializer = serializers.MakeOrderSerializer(order,request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
         
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         order.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

