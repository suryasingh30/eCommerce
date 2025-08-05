from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum, Count
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from .filters import ProductFilter
from orders.models import OrderItem
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView

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

class ProductReportView(APIView):
    permission_classes=[IsAdminUser]

    def get(self, request):
        sort=request.query_params.get('sort')
        category_slug=request.query_params.get('category')

        queryset=Product.objects.annotate(
            total_sold=Sum('orderitem__quantity')
        ).filter(total_sold__isnull=False)

        if category_slug:
            queryset=queryset.filter(category__slug=category_slug)

        if sort == 'most_sold':
            queryset=queryset.order_by('-total_sold')

        elif sort == 'least_sold':
            queryset=queryset.order_by('total_sold')

        data=[
            {
                'product': product.title,
                'category': product.category.name,
                'sold': product.total_sold or 0
            }
            for product in queryset
        ]
        return Response(data)