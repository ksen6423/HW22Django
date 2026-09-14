from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.services import category_products
from catalog.views import HomeView, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView
from catalog.views import ContactsView

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("", ProductListView.as_view(), name="products_list"),
    path("catalog/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="products_detail"),
    path("catalog/create", ProductCreateView.as_view(), name="products_create"),
    path("catalog/<int:pk>/update/", ProductUpdateView.as_view(), name="products_update"),
    path("catalog/<int:pk>/delete/", ProductDeleteView.as_view(), name="products_delete"),
    path('category/<int:category_id>/', category_products, name='category_products'),
]
