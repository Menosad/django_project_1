from django.urls import path

from catalog.apps import MyappConfig
from catalog.views import index, contacts, product

app_name = MyappConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', product, name='product'),
]
