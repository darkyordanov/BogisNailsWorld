from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from bogis_nails.account.forms import AccountRegisterForm

UserModel = get_user_model()

# from django.contrib.auth.decorators import login_required

class RegisterAccountView(views.CreateView):
    # TODO: fix authentication form for register
    # TODO: update 'account' -> 'profile'
    
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
    redirect_authenticated_user = True
    
    
class LogoutAccountView(auth_views.LogoutView):
    # remove the template_name attribute
    # success_url = reverse_lazy('index')
    
    next_page = '/'


class DetailsAccountView(views.DetailView, LoginRequiredMixin):
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
    
class EditAccountView(views.UpdateView):
    pass


class DeleteAccountView(views.DeleteView):
    pass