from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('bogis_nails.core.urls')),
    path('catalog/', include('bogis_nails.catalog.urls')),
    path('booking/', include('bogis_nails.booking.urls')),
    path('products/', include('bogis_nails.product.urls')),
    path('account/', include('bogis_nails.account.urls')),
    path('cart/', include('bogis_nails.cart.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'bogis_nails.core.views.custom_404'