from django.core.cache import cache
from django.shortcuts import render

from catalog.models import Product
from config.settings import CACHES_ENABLED

def get_product_from_cache():
    """
    Получает данные продукта из кэша, если кэш пуст, получает данные из БД.
    """
    if not CACHES_ENABLED:
        return Product.objects.all()
    key = "product_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


def get_products_by_category(category_id):
    return Product.objects.filter(category_id=category_id).select_related('category')

def category_products(request, category_id):
    products = get_products_by_category(category_id)
    return render(request, 'category_products.html', {'products': products})


