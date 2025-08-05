from django.urls import path
from .views import AddToCartView, CartView, CheckoutView

urlpatterns = [
    path('checkout', CheckoutView.as_view(), name='checkout'),
    path('add/', AddToCartView.as_view(), name='add-to-cart'),
    path('', CartView.as_view(), name='view-cart')
]