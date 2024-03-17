from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from bogis_nails.account.models import Profile

# from bogis_nails.account.models import Profile

UserModel = get_user_model()


class AccountUserChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = UserModel
        fields = '__all__'
        # we can add additional custom fields to the form
        # fields = auth_forms.UserChangeForm.Meta.fields + ('birth_date',)
        
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
            # 'birth_date': forms.DateInput(attrs={'placeholder': 'Birth date'}),
            # 'profile_picture': forms.ImageField(),
        }
        
        
class AccountRegisterForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email', 'password1', 'password2')
        
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            # 'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
            # 'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
            # 'birth_date': forms.DateInput(attrs={'placeholder': 'Birth date'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        
        if commit:
            user.save()
            Profile.objects.create(user=user)
            
        return user


# Update form when user is success register to update her/his profile information later
# class AccountUpdateForm(auth_forms.UserCreationForm):
#     age = forms.IntegerField()

#     # Other fields of `Profile`
