from django.urls import path

from bogis_nails.account.views import \
    RegisterAccountView, LoginAccountView, LogoutAccountView

urlpatterns = (
    path('register/', RegisterAccountView.as_view(), name='register'),
    # path('login/', LoginAccountView.as_view(), name='login'),
    # path('logout/', LogoutAccountView.as_view(), name='logout'),
)