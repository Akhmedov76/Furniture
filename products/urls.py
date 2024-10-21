from django.urls import path

from products import views

app_name = 'products'
urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('product-detail/', views.ProductDetailView.as_view(), name='product_detail'),
]
