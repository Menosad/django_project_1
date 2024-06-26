from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from advertising.models import Advertising


class AdvertisingCreateView(CreateView):
    model = Advertising
    fields = ('name', 'description', 'duration')
    success_url = reverse_lazy('catalog:index')


class AdvertisingListView(ListView):
    model = Advertising


