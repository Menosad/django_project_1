from django.core.cache import cache

from catalog.models import Category
from config.settings import CACHE_ENABLED


def get_product_list_from_cache(pk: int) -> list:
    """Обращение к кэшу, если кэш выключен, то обращается к бд"""
    if CACHE_ENABLED:
        key = f'product_list{pk}'
        product_list = cache.get(key)
        if product_list is None:
            product_list = Category.objects.get(pk=pk).products.all()
            cache.set(key, product_list)
    else:
        product_list = Category.objects.get(pk=pk).products.all()
    return product_list
