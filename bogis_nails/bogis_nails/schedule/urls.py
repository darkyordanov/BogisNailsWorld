from django.urls import path

from bogis_nails.schedule.views import schedule

urlpatterns = (
    path('', schedule, name='schedule'),
)