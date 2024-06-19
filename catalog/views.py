import os
from django.shortcuts import render

from catalog.models import Product


def index(request):
    products_list = Product.objects.all()
    context = {
        'products_list': products_list
    }
    return render(request, os.path.join('catalog', 'index.html'), context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('UserName')
        email = request.POST.get('UserEmail')
        phone_number = request.POST.get('UserPhone')
        print(f"FEEDBACK request:\n"
              f"user: {name}\n"
              f"email: {email}\n"
              f"phone number: {phone_number}")
    return render(request, os.path.join('catalog', 'contacts.html'))
