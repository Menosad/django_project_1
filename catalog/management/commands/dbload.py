import json
from catalog.models import Product, Category
from django.core.management import BaseCommand
import os


class Command(BaseCommand):
    data_path = os.path.abspath("catalog_data.json")

    @staticmethod
    def get_data():
        with open(Command.data_path, encoding="utf-8") as file:
            data_str = file.read()
            data = json.loads(data_str)
        return data

    @staticmethod
    def get_category_data():
        data = Command.get_data()
        res_list = []
        for item in data:
            if item["model"] == "catalog.category":
                data_dict = {
                    "pk": item["pk"],
                    "name": item["fields"]["name"],
                    "description": item["fields"]["description"],
                }
                res_list.append(data_dict)
        return res_list

    @staticmethod
    def get_product_data():
        data = Command.get_data()
        res_list = []
        for item in data:
            if item["model"] == "catalog.product":
                category = Category.objects.get(pk=item["fields"]["category"])
                data_dict = {
                    "pk": item["pk"],
                    "name": item["fields"]["name"],
                    "category": category,
                    "avatar": item["fields"]["avatar"],
                    "price": item["fields"]["price"],
                    "created_at": item["fields"]["created_at"],
                    "updated_at": item["fields"]["updated_at"],
                }
                res_list.append(data_dict)
        return res_list

    def handle(self, *args, **options):
        category_list = Command.get_category_data()
        Category.objects.all().delete()
        category_for_create = []
        for category_item in category_list:
            category_for_create.append(Category(**category_item))
        Category.objects.bulk_create(category_for_create)
        product_list = Command.get_product_data()
        product_for_create = []
        for product_item in product_list:
            product_for_create.append(Product(**product_item))
        Product.objects.bulk_create(product_for_create)
