from django.core.cache import cache

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


def get_products_by_category(category_id: int):
    queryset = Product.objects.filter(
        category_id=category_id
    ).select_related("category")

    if not CACHES_ENABLED:
        return queryset

    cache_key = f"category_{category_id}"
    products = cache.get(cache_key)

    if products is None:
        products = list(queryset)
        cache.set(cache_key, products, timeout=60)

    return products
