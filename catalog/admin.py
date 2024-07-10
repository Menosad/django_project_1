from django.contrib import admin
from catalog.models import Category, Product, Blog, Version


@admin.register(Category)
class CatalogAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = ("name", "description")


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "preview", "created_at", "update_at", "views")
    list_filter = ("title", "views", "update_at")
    search_fields = ("title", "content")


@admin.register(Version)
class AdminVersion(admin.ModelAdmin):
    list_display = ('name', 'number', 'is_current', 'product',)
    list_filter = ('name',)
