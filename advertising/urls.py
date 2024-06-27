from django.urls import path

from advertising.apps import AdvertisingConfig
from advertising.views import AdvertisingCreateView, AdvertisingListView, AdvertisingDetailView, AdvertisingUpdateView, AdvertisingDeleteView

app_name = AdvertisingConfig.name

urlpatterns = [
     path('create/', AdvertisingCreateView.as_view(), name='create'),
     path('list/', AdvertisingListView.as_view(), name='list'),
     path('detail/<int:pk>', AdvertisingDetailView.as_view(), name='detail'),
     path('edit/<int:pk>', AdvertisingUpdateView.as_view(), name='edit'),
     path('delete/<int:pk>', AdvertisingDeleteView.as_view(), name='delete'),
     ]
