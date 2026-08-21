from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomeView, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView
from catalog.views import ContactsView

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("", ProductListView.as_view(), name="products_list"),
    path("catalog/<int:pk>/", ProductDetailView.as_view(), name="products_detail"),
    path("catalog/create", ProductCreateView.as_view(), name="products_create"),
    path("catalog/<int:pk>/update/", ProductUpdateView.as_view(), name="products_update"),
    path("catalog/<int:pk>/delete/", ProductDeleteView.as_view(), name="products_delete")
]
