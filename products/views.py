from django.shortcuts import render
from django.views.generic import TemplateView

from products.models import ProductModel


class ProductDetailView(TemplateView):
    template_name = 'products/product-detail.html'


class ProductListView(TemplateView):
    template_name = 'products/product-list.html'
    model = ProductModel
    context_object_name = 'products'