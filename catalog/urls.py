from django.urls import path

from catalog.apps import MyappConfig
from catalog.views import (
    CatalogListView,
    CatalogTemplateView,
    ProductDetailView,
    BlogListView,
    BlogCreateView,
    BlogDetailView,
    BlogUpdateView,
    BlogDeleteView,
)

app_name = MyappConfig.name

urlpatterns = [
    path("", CatalogListView.as_view(), name="index"),
    path("contacts/", CatalogTemplateView.as_view(), name="contacts"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product"),
    path("blog_list/", BlogListView.as_view(), name="blog_list"),
    path("blog_form/", BlogCreateView.as_view(), name="create"),
    path("blog_detail/<int:pk>/", BlogDetailView.as_view(), name="detail"),
    path("blog_form/<int:pk>/", BlogUpdateView.as_view(), name="edit"),
    path("blog_delete/<int:pk>/", BlogDeleteView.as_view(), name="delete_blog"),
]
