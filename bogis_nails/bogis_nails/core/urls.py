from django.urls import path
from django.conf.urls import handler404

from bogis_nails.core.views import \
    index, custom_404, price_list

urlpatterns = (
    path('', index, name='index'),
    
    path('price_list/', price_list, name='price list'),
)

handler404 = custom_404 