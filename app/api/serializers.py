from rest_framework import serializers
from app import models

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Review
        fields = '__all__'

class MakeOrderSerializer(serializers.ModelSerializer):
    # reviews = serializers.StringRelatedField(many=True, read_only=True)
    #reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    reviews = serializers.HyperlinkedRelatedField(many=True, read_only=True,view_name='reivew_link')
    class Meta:
        model = models.MakeOrder
        fields = '__all__'

class DeliveryOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DeliveryOrder
        fields = '__all__'
