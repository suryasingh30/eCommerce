from django.urls import path
from .views import ProductViewSet, CategoryViewSet, ProductReportView

product_list = ProductViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
product_detail = ProductViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
category_list = CategoryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
category_detail = CategoryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
urlpatterns = [
    # product
    path('', product_list, name='product-list'),
    path('<int:pk>/', product_detail, name='product-detail'),

    # category
    path('categories/', category_list, name='category-list'),
    path('categories/<int:pk>/', category_detail, name='category-detail'),

    # product report bas admins
    path('reports/products/', ProductReportView.as_view(), name='product-report'),
]
