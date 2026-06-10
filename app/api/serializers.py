from rest_framework import serializers
from app import models

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Review
        fields = '__all__'

class MakeOrderSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = models.MakeOrder
        fields = '__all__'

class DeliveryOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DeliveryOrder
        fields = '__all__'
