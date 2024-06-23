from django.shortcuts import render, get_object_or_404
from catalog.models import Product


def index(request):
    products_list = Product.objects.all()
    context = {
        'products_list': products_list,
        'title': 'Каталог'
    }
    return render(request, 'catalog/index.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('UserName')
        email = request.POST.get('UserEmail')
        phone_number = request.POST.get('UserPhone')
        print(f"FEEDBACK request:\n"
              f"user: {name}\n"
              f"email: {email}\n"
              f"phone number: {phone_number}")
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)


def product(request, pk):
    prod = get_object_or_404(Product, pk=pk)
    context = {
        'prod': prod,
        'title': prod.name
    }
    return render(request, 'catalog/product.html', context)
