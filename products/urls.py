from django.urls import path, include
from products.api.viewset import ProductDetailView, ProductsListView
urlpatterns = [
    path('products', ProductsListView.as_view(), name='products_list'),
    path('product-details/<int:pk>',
         ProductDetailView.as_view(), name='product_details'),
    path('api-auth/', include('rest_framework.urls'))
]
