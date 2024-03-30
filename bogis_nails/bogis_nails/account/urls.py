from django.urls import include, path

from bogis_nails.account.views import \
    RegisterAccountView, LoginAccountView, LogoutAccountView, \
    DetailsAccountView, EditAccountView, DeleteAccountView

urlpatterns = (
    path('register/', RegisterAccountView.as_view(), name='register'),
    path('login/', LoginAccountView.as_view(), name='login'),
    path('logout/', LogoutAccountView.as_view(), name='logout'),
    
    path('<int:pk>/', include([
        path('', DetailsAccountView.as_view(), name='details account'),
        path('edit/', EditAccountView.as_view(), name='edit account'),
        path('delete/', DeleteAccountView.as_view(), name='delete account'),
    ])),
)