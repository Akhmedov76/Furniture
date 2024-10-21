from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'pages/home.html'


class ErrorView(TemplateView):
    template_name = 'pages/404.html'


class AboutView(TemplateView):
    template_name = 'pages/about-us.html'


class CartView(TemplateView):
    template_name = 'ordering/cart.html'


class CheckoutView(TemplateView):
    template_name = 'ordering/checkout.html'
