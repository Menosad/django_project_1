from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView

from catalog.models import Product


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

# def product(request, pk):
#     prod = get_object_or_404(Product, pk=pk)
#     context = {
#         'prod': prod,
#         'title': prod.name
#     }
#     return render(request, 'catalog/product.html', context)
