from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# from bogis_nails.account.models import CustomAcc


class AccountRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
            # 'birth_date': forms.DateInput(attrs={'placeholder': 'Birth date'}),
        }