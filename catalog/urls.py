from django.urls import path

from catalog.apps import MyappConfig
from catalog.views import (
    ProductListView,
    CatalogTemplateView,
    ProductDetailView,
    BlogListView,
    BlogCreateView,
    BlogDetailView,
    BlogUpdateView,
    BlogDeleteView, ProductCreateView, ProductUpdateView,
)

app_name = MyappConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="index"),
    path("create_product", ProductCreateView.as_view(), name="create_product"),
    path("edit_product/<int:pk>", ProductUpdateView.as_view(), name="edit_product"),
    path("contacts/", CatalogTemplateView.as_view(), name="contacts"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product"),
    path("blog_list/", BlogListView.as_view(), name="blog_list"),
    path("blog_form/", BlogCreateView.as_view(), name="create"),
    path("blog_detail/<int:pk>/", BlogDetailView.as_view(), name="detail"),
    path("blog_form/<int:pk>/", BlogUpdateView.as_view(), name="edit"),
    path("blog_delete/<int:pk>/", BlogDeleteView.as_view(), name="delete_blog"),
]
