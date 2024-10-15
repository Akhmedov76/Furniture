from django.urls import path

from products import views

app_name = 'products'
urlpatterns = [
    path('product-list/', views.ProductListView.as_view(), name='product_list'),
    path('product-detail/', views.ProductDetailView.as_view(), name='product_detail'),
]
