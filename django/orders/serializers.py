from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    """Order Serializer - handles data serialization"""
    
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('total_price', 'created_at', 'updated_at')