from rest_framework import serializers
from .models import Order, OrderItem
from products.models import Product

class OrderItemSerializer(serializers.ModelSerializer):
    peorduct = serializers.StringRelatedField()

    class Meta:
        model=OrderItem
        fields=['id', 'product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model=Order
        fields=['id', 'ordered_at', 'items']