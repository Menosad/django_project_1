from django.urls import path

from catalog.apps import MyappConfig
from catalog.views import CatalogListView, CatalogTemplateView, ProductDetailView

app_name = MyappConfig.name

urlpatterns = [
    path('', CatalogListView.as_view(), name='index'),
    path('contacts/', CatalogTemplateView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
]
