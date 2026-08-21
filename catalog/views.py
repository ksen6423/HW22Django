from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, UpdateView, CreateView

from catalog.models import Product

class HomeView(TemplateView):
    template_name = "home.html"

class ContactsView(TemplateView):
    template_name = "contacts.html"

class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(CreateView):
    model = Product
    fields = ("name", "description", "image", "category", "price", "created_at", "updated_at")
    success_url = reverse_lazy('catalog:products_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ("name", "description", "image", "category", "price", "created_at", "updated_at")
    success_url = reverse_lazy('catalog:products_list')

class ProductDeleteView(DetailView):
    model = Product
    success_url = reverse_lazy('catalog:products_list')
