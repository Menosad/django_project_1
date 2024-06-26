from django.urls import path

from advertising.apps import AdvertisingConfig
from advertising.views import AdvertisingCreateView, AdvertisingListView

app_name = AdvertisingConfig.name

urlpatterns = [
     path('create/', AdvertisingCreateView.as_view(), name='create'),
     path('list/', AdvertisingListView.as_view(), name='list')
]
