from django.urls import path

from bogis_nails.cart.views import \
    cart_summary, cart_add, cart_update, cart_delete

urlpatterns = [
    path('', cart_summary, name='cart summary'),
    path('add/', cart_add, name='cart add'),
    path('update/', cart_update, name='cart update'),
    path('delete/', cart_delete, name='cart delete'),
]
