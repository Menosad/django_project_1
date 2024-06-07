import os
from django.shortcuts import render


def index(request):
    return render(request, os.path.join('catalog', 'index.html'))


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
