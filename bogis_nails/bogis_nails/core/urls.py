from django.urls import path

from bogis_nails.core.views import index

urlpatterns = (
    path('', index, name='index'),
)
