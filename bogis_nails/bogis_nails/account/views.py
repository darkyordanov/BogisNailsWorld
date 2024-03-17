from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views
from django.contrib.auth import get_user_model
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import UserPassesTestMixin

from bogis_nails.account.forms import AccountRegisterForm
from bogis_nails.account.models import Profile

UserModel = get_user_model()


class UserOwnsProfileMixin(UserPassesTestMixin):
    def test_func(self):
        # Retrieve the profile ID from the URL parameters
        profile_id = self.kwargs.get('pk')
        
        # Retrieve the requested profile object
        profile = get_object_or_404(Profile, pk=profile_id)
        
        # Check if the requested profile belongs to the currently logged-in user
        return profile.user == self.request.user
    

class RegisterAccountView(views.CreateView):
    # TODO: fix authentication form for register
    # TODO: update 'account' -> 'profile'
    
    # UserCreationForm overright it
    form_class = AccountRegisterForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('login')
    
    # def get_success_url(self):
    #     return reverse_lazy('details account', kwargs={
    #         'pk': self.object.pk,
    #     })


class LoginAccountView(auth_views.LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('index')
    redirect_authenticated_user = True
    
    
class LogoutAccountView(auth_mixins.LoginRequiredMixin, auth_views.LogoutView):
    next_page = '/'


class DetailsAccountView(auth_mixins.LoginRequiredMixin, UserOwnsProfileMixin, views.DetailView):
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