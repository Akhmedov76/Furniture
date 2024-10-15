from django.shortcuts import render
from django.views.generic import TemplateView


class BlogDetailView(TemplateView):
    template_name = 'blog-detail.html'


class BlogListView(TemplateView):
    template_name = 'blog-list.html'