from django.urls import path

from users import views

app_name = 'users'
urlpatterns = [
    path('account/', views.UserAccountView.as_view(), name='account'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('reset-password/', views.UserResetPasswordView.as_view(), name='Reset_password'),
    path('wishlist/', views.UserWishListView.as_view(), name='user_wish_list'),
]
