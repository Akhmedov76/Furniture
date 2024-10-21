from django.urls import path

from contact import views

app_name = 'contact'

urlpatterns = [

    path('contact-us/', views.ContactView.as_view(), name='contact-us'),

]
