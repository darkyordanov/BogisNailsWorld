from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views
from django.contrib.auth import get_user_model
from django.contrib.auth import mixins as auth_mixins

from bogis_nails.account.forms import AccountRegisterForm

UserModel = get_user_model()


class RegisterAccountView(views.CreateView):
    # TODO: fix authentication form for register
    # TODO: update 'account' -> 'profile'
    
    # UserCreationForm overright it
    form_class = AccountRegisterForm
    template_name = 'account/register.html'
    
    def get_success_url(self):
        return reverse_lazy('details account', kwargs={
            'pk': self.object.pk,
        })


class LoginAccountView(auth_views.LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('index')
    redirect_authenticated_user = True
    
    
class LogoutAccountView(auth_mixins.LoginRequiredMixin, auth_views.LogoutView):
    next_page = '/'


class DetailsAccountView(auth_mixins.LoginRequiredMixin, views.DetailView):
    # not sure, about details account, because
    # when u are in your profile
    template_name = 'account/details_account.html'
    queryset = UserModel.objects.all()
    # context_object_name = 'profile'  # Define the context object name
    
    # def get_object(self, queryset=None):
    #     # Return the current logged-in user's profile
    #     return self.request.user

    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # You can add additional context data here if needed
    #     return context
    
class EditAccountView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    template_name = 'account/edit_account.html'
    queryset = UserModel.objects.all()
    

class DeleteAccountView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    pass