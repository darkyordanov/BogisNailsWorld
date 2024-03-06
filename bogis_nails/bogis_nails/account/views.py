from django.urls import reverse_lazy
from django.views.generic import CreateView

from bogis_nails.account.forms import AccountRegisterForm

class RegisterAccountView(CreateView):
    # UserCreationForm overright it
    form_class = AccountRegisterForm
    template_name = 'account/register.html'
    
    def get_success_url(self) -> str:
        return reverse_lazy('account', kwargs={
            'pk': self.object.pk,
        })


class LoginAccountView():
    pass


class LogoutAccountView():
    pass