from django.shortcuts import render
from django.views.generic import TemplateView


class ProductDetailView(TemplateView):
    template_name = 'product-detail.html'


class ProductListView(TemplateView):
    template_name = 'product-list.html'