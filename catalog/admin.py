from django.contrib import admin
from catalog.models import Category


@admin.register(Category)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)

