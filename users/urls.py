from django.urls import path

from users import views
from users.views import verify_email

app_name = 'users'
urlpatterns = [
    path('account/', views.UserAccountView.as_view(), name='account'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    # path('logout/', views.LogoutView.as_view(), name='logout'),
    path('reset-password/', views.UserResetPasswordView.as_view(), name='reset-password'),
    # path('wishlist/', views.UserWishListView.as_view(), name='user_wish_list'),
    path('verify-email/<str:uidb64>/<str:token>/', verify_email, name='verify-email'),

]
