from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views

from bogis_nails.account.forms import AccountRegisterForm

# from django.contrib.auth.decorators import login_required

class RegisterAccountView(views.CreateView):
    # UserCreationForm overright it
    form_class = AccountRegisterForm
    template_name = 'account/register.html'
    
    def get_success_url(self):
        return reverse_lazy('account', kwargs={
            'pk': self.object.pk,
        })


class LoginAccountView(auth_views.LoginView):
    # redirect to home page
    template_name = 'account/login.html'
    success_url = reverse_lazy('index')

class LogoutAccountView(auth_views.LogoutView):
    # redirect to home page
    pass


class DetailsAccountView(views.DetailView):
    # not sure, about details account, because
    # when u are in your profile
    pass


class EditAccountView(views.UpdateView):
    pass


class DeleteAccountView(views.DeleteView):
    pass