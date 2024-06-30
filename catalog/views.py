from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    TemplateView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from pytils.translit import slugify

from catalog.models import Product, Blog


class CatalogListView(ListView):
    model = Product
    template_name = "catalog/index.html"


class CatalogTemplateView(TemplateView):
    template_name = "catalog/contacts.html"

    def post(self, *args, **kwargs):
        name = self.request.POST.get("UserName")
        mail = self.request.POST.get("UserEmail")
        phone = self.request.POST.get("UserPhone")
        print(f"Запрос на обратную связь:\n{name}\n{mail}\n{phone}")
        return render(self.request, self.template_name)


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product.html"


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        list_objects = super().get_queryset(*args, **kwargs)
        new_list = list_objects.filter(is_published=True)
        return new_list


class BlogCreateView(CreateView):
    model = Blog
    fields = (
        "title",
        "content",
        "preview",
    )

    def form_valid(self, form):
        if form.is_valid():
            obj = form.save()
            obj.slug = slugify(obj.title)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("catalog:detail", args=[self.kwargs.get("pk")])


class BlogUpdateView(UpdateView):
    model = Blog
    fields = (
        "title",
        "content",
        "preview",
    )
    success_url = reverse_lazy("catalog:blog_list")

    def form_valid(self, form):
        if form.is_valid():
            obj = form.save()
            obj.slug = slugify(obj.title)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("catalog:detail", args=[self.kwargs.get("pk")])


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        obj = super().get_object()
        obj.views += 1
        obj.save()
        return obj


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("catalog:blog_list")
