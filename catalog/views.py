from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView

from catalog.models import Product


class CatalogListView(ListView):
    model = Product
    template_name = 'catalog/index.html'


# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('UserName')
#         email = request.POST.get('UserEmail')
#         phone_number = request.POST.get('UserPhone')
#         print(f"FEEDBACK request:\n"
#               f"user: {name}\n"
#               f"email: {email}\n"
#               f"phone number: {phone_number}")
#     context = {
#         'title': 'Контакты'
#     }
#     return render(request, 'catalog/contacts.html', context)
class CatalogTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, form):
        if form == 'POST':
            print('POST')


def product(request, pk):
    prod = get_object_or_404(Product, pk=pk)
    context = {
        'prod': prod,
        'title': prod.name
    }
    return render(request, 'catalog/product.html', context)
