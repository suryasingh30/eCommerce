from rest_framework import serializers
from .models import Wishlist
from products.models import Product

class WishlistSerializer(serializers.ModelSerializer):
    products=serializers.StringRelatedField(many=True)

    class Meta:
        model=Wishlist
        fields=['id', 'user', 'products']