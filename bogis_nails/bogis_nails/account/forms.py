from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from bogis_nails.account.models import Profile

UserModel = get_user_model()


class AccountRegisterForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email', 'password1', 'password2')
        
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
    }))

    def save(self, commit=True):
        user = super().save(commit=False)
        
        if commit:
            user.save()
            Profile.objects.create(user=user)

        return user
    

class AccountLoginForm(auth_forms.AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your email address',
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
    }))
    

class AccountUpdateForm(auth_forms.UserChangeForm):
    birth_date = forms.DateField(required=False)
    profile_picture = forms.ImageField(required=False)
    new_password1 = forms.CharField(label="New Password", strip=False, widget=forms.PasswordInput, required=False)
    new_password2 = forms.CharField(label="Confirm New Password", strip=False, widget=forms.PasswordInput, required=False)

    class Meta:
        model = UserModel
        fields = ('email', 'first_name', 'last_name', 'birth_date', 'profile_picture', 'new_password1', 'new_password2')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.initial['birth_date'] = instance.profile.birth_date
            self.initial['profile_picture'] = instance.profile.profile_picture
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        instance = getattr(self, 'instance', None)
        
        # Check if email exists and is different from the current instance's email
        if email and UserModel.objects.exclude(pk=instance.pk).filter(email=email).exists():
            raise forms.ValidationError("This email is already in use. Please choose a different email.")
        
        return email
            
    def clean_new_password2(self):
        new_password1 = self.cleaned_data.get("new_password1")
        new_password2 = self.cleaned_data.get("new_password2")
        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError("The two password fields didn't match.")
        return new_password2

    def save(self, commit=True):
        user = super().save(commit=False)
        profile = user.profile
        profile.birth_date = self.cleaned_data['birth_date']

        if 'profile_picture' in self.cleaned_data:
            profile.profile_picture = self.cleaned_data['profile_picture']

        new_password = self.cleaned_data['new_password1']

        if new_password:
            user.set_password(new_password)
        
        if commit:
            user.save()
            profile.save()
        return user