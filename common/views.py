from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'


class ErrorView(TemplateView):
    template_name = '404.html'


class AboutView(TemplateView):
    template_name = 'about-us.html'


class CartView(TemplateView):
    template_name = 'cart.html'


class CheckoutView(TemplateView):
    template_name = 'checkout.html'
