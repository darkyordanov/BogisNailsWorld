from django.urls import path

from bogis_nails.booking.views import booking

urlpatterns = (
    path('', booking, name='booking'),
)