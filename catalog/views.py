from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, UpdateView, CreateView

from catalog.forms import ProductForm
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
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products_list')
    method = "POST"

    def product_create(self, request):
        if request.method == "POST":
            form = ProductForm(self.request.POST)
            if form.is_valid():
                form.save()
                return redirect("product_list")
        else:
            form = ProductForm()
        return render(request, "product_form.html", {"form": form})


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products_list')
    method = "POST"

    def product_update(self, request, pk):
        product = Product.objects.get(pk=pk)
        if request.method == "POST":
            form = ProductForm(self.request.POST, instance=product)
            if form.is_valid():
                form.save()
                return redirect("product_list")
        else:
            form = ProductForm(instance=product)
        return render(request, "product_form.html", {"form": form})


class ProductDeleteView(DetailView):
    model = Product
    success_url = reverse_lazy('catalog:products_list')
