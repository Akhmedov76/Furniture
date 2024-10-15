from django.urls import path

from common import views

app_name = 'common'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),

    path('cart/', views.CartView.as_view, name='cart_detail'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('404/', views.ErrorView.as_view(), name='404'),
]
