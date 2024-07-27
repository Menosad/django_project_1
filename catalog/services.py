from django.core.cache import cache

from catalog.models import Category, Product
from config.settings import CACHE_ENABLED


def get_current_version_list(lst: list):
    prod_list = []
    for object in lst:
        product = Product.objects.get(pk=object.pk)
        if Product.objects.get(pk=object.pk).versions.filter(is_current=True):
            product.version = Product.objects.get(pk=object.pk).versions.filter(is_current=True).get()
        else:
            product.version = None
        prod_list.append(product)
    return prod_list


def get_product_list_from_cache(pk: int) -> list:
    """Обращение к кэшу, если кэш выключен, то обращается к бд"""
    if CACHE_ENABLED:
        key = f'product_list{pk}'
        products_list = cache.get(key)
        if products_list is None:
            products_list = Category.objects.get(pk=pk).products.all()
            prod_list = get_current_version_list(products_list)
            cache.set(key, prod_list)
    else:
        products_list = Category.objects.get(pk=pk).products.all()

    prod_list = get_current_version_list(products_list)
    return prod_list
