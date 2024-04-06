from django.urls import path
from django.conf.urls import handler404

from bogis_nails.core.views import \
    index, price_list, custom_404

urlpatterns = (
    path('', index, name='index'),

    path('price_list/', price_list, name='price list'),
)

