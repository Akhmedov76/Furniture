from django.urls import path
from blogs import views

app_name = 'blogs'
urlpatterns = [
    path('blog/', views.BlogListView.as_view(), name='blog_list'),
    path('blog-detail/', views.BlogDetailView.as_view(), name='blog_detail'),
]
