import os
from django.shortcuts import render


def index(request):
    return render(request, os.path.join('catalog', 'index.html'))


def contacts(request):
    return render(request, os.path.join('catalog', 'contacts.html'))
