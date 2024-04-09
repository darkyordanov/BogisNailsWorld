from django.db.models.base import Model as Model
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views
from django.contrib.auth import get_user_model
from django.contrib.auth import mixins as auth_mixins
from django.contrib import messages

from bogis_nails.account.forms import \
    AccountLoginForm, AccountRegisterForm, AccountUpdateForm
from bogis_nails.common.user_owns_profile_mixin import UserOwnsProfileMixin

UserModel = get_user_model()

class RegisterAccountView(views.CreateView):
    # TODO: fix authentication form for register
    # TODO: update 'account' -> 'profile'
    
    # UserCreationForm overright it
    form_class = AccountRegisterForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('login')
    

class LoginAccountView(auth_views.LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('index')
    redirect_authenticated_user = True    
    authentication_form = AccountLoginForm
    
    # def form_valid(self, form):
    #     auth_login(self.request, form.get_user())
    #     return super().form_valid(form)
    
    
class LogoutAccountView(auth_mixins.LoginRequiredMixin, auth_views.LogoutView):
    next_page = '/'


class DetailsAccountView(auth_mixins.LoginRequiredMixin, UserOwnsProfileMixin, views.DetailView):
    template_name = 'account/details_account.html'
    queryset = UserModel.objects.all()
    

class EditAccountView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    template_name = 'account/edit_account.html'
    queryset = UserModel.objects.all()
    form_class = AccountUpdateForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account'] = self.get_object()
        return context

    def get_success_url(self):
        return reverse_lazy('details account', kwargs={
            'pk': self.object.pk
        })


class DeleteAccountView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    template_name = 'account/delete_account.html'
    queryset = UserModel.objects.all()
    success_url = reverse_lazy('index')
    
    def get_object(self, queryset=None):
        return self.request.user
    