from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import MyappConfig
from catalog.views import (
    CatalogTemplateView,
    ProductDetailView,
    BlogListView,
    BlogCreateView,
    BlogDetailView,
    BlogUpdateView,
    BlogDeleteView, ProductCreateView, ProductUpdateView, VersionDetailView, VersionDeleteView, CategoriesListView,
    CategoryDetailView,
)

app_name = MyappConfig.name

urlpatterns = [
    path("product_list/<int:pk>", CategoryDetailView.as_view(), name="product_list"),
    path("", CategoriesListView.as_view(), name="main"),
    path("create_product", ProductCreateView.as_view(), name="create_product"),
    path("edit_product/<int:pk>", ProductUpdateView.as_view(), name="edit_product"),
    path("contacts/", CatalogTemplateView.as_view(), name="contacts"),
    path("product/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product"),
    path("blog_list/", BlogListView.as_view(), name="blog_list"),
    path("blog_form/", BlogCreateView.as_view(), name="create"),
    path("blog_detail/<int:pk>/", BlogDetailView.as_view(), name="detail"),
    path("blog_form/<int:pk>/", BlogUpdateView.as_view(), name="edit"),
    path("blog_delete/<int:pk>/", BlogDeleteView.as_view(), name="delete_blog"),
    path("version_detail/<int:pk>/", VersionDetailView.as_view(), name="version_detail"),
    path("version_delete/<int:pk>/", VersionDeleteView.as_view(), name="version_delete"),
]
