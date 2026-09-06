from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, UpdateView, CreateView, DeleteView


from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product


class HomeView(TemplateView):
    template_name = "home.html"


class ContactsView(TemplateView):
    template_name = "contacts.html"


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
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

    permission_required = 'catalog.add_product'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
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

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product") and user.has_perm("catalog.can_delete_product"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products_list')
