from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from advertising.models import Advertising


class AdvertisingCreateView(CreateView):
    model = Advertising
    fields = ('name', 'description', 'avatar')
    success_url = reverse_lazy('advertising:list')


class AdvertisingListView(ListView):
    model = Advertising


class AdvertisingDetailView(DetailView):
    model = Advertising


class AdvertisingUpdateView(UpdateView):
    model = Advertising
    fields = ('name', 'avatar')


class AdvertisingDeleteView(DeleteView):
    model = Advertising
    success_url = reverse_lazy('advertising:list')
