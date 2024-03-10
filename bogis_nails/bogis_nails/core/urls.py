from django.urls import path
from django.conf.urls import handler404

from bogis_nails.core.views import index, custom_404

urlpatterns = (
    path('', index, name='index'),
)

handler404 = custom_404 