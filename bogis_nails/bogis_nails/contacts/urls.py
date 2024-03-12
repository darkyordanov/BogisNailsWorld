from django.urls import path

from bogis_nails.contacts.views import contacts

urlpatterns = (
    path('', contacts, name='contacts'),
)
