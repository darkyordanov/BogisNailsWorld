from django.urls import path
from django.conf.urls import handler404

from django.conf import settings
from django.conf.urls.static import static


from bogis_nails.core.views import \
    index, custom_404, price_list

urlpatterns = [
    path('', index, name='index'),
    
    path('price_list/', price_list, name='price list'),
]

handler404 = custom_404 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)