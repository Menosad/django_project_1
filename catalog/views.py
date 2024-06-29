from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView

from catalog.models import Product, Blog


class CatalogListView(ListView):
    model = Product
    template_name = 'catalog/index.html'


class CatalogTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, *args, **kwargs):
        name = self.request.POST.get('UserName')
        mail = self.request.POST.get('UserEmail')
        phone = self.request.POST.get('UserPhone')
        print(f"Запрос на обратную связь:\n{name}\n{mail}\n{phone}")
        return render(self.request, self.template_name)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'


class BlogListView(ListView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview',)
    success_url = reverse_lazy('catalog:blog_list')
