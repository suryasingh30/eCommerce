from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Wishlist
from products.models import Product

# Create your views here.
class WishlistView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request):
        wishlist, _=Wishlist.objects.get_or_create(user=request.user)
        return Response({"products": [str(p) for p in wishlist.products.all()]})
    
    def post(self, request):
        product_id=request.data.get('product_id')
        product=Product.objects.filter(id=product_id).first()
        if not product:
            return Response({"error": "Product not found"}, status=404)
        
        wishlist, _=Wishlist.objects.get_or_create(user=request.user)
        wishlist.products.add(product)
        return Response({"message": "Product added to wishlist"})
    
    def delete(self, request):
        product_id=request.data.get('product_id')
        wishlist=Wishlist.objects.filter(user=request.user).first()
        if not wishlist:
            return Response({"error": "Wishlist not found"}, status=404)
        
        wishlist.products.remove(product_id)
        return Response({"message": "Product removed from wishlist"})