from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from .filters import ProductFilter

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin #type: ignore

class ProductPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated(), IsAdmin()]
        return [permissions.AllowAny()]

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

    # filtering, searching or ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['title', 'description']
    ordering_fields = ['price', 'created_at', 'sold_count']

    def get_queryset(self):
        return Product.objects.annotate(
            sold_count=Sum('order_items__quantity')
        ).order_by('-created_at')

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated(), IsAdmin()]
        return [permissions.AllowAny()]
