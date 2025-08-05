from rest_framework import serializers
from .models import Order, OrderItem
from products.models import Product

class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()

    class Meta:
        model=OrderItem
        fields=['id', 'product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model=Order
        fields=['id', 'ordered_at', 'items', 'total_price']

    def get_total_price(self, obj):
        return sum(item.product.price * item.quantity for item in obj.items.all())