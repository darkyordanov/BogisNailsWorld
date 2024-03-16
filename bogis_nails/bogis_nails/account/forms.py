from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

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
        # fields = auth_forms.UserChangeForm.Meta.fields + ('birth_date',)
        
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            # 'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
            # 'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
            # 'birth_date': forms.DateInput(attrs={'placeholder': 'Birth date'}),
        }
        
        
    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = (UserModel.USERNAME_FIELD,)
        # fields = auth_forms.UserCreationForm.Meta.fields + ("age",)

    # def save(self, commit=True):
    #     user = super().save(commit=commit)

    #     profile = Profile(
    #         user=user,
    #         # birth_date=self.cleaned_data["birth_date"],
    #         # profile_picture=self.cleaned_data["profile_picture"],
    #     )

    #     if commit:
    #         profile.save()

    #     return user

# Update form when user is success register to update her/his profile information later
# class AccountUpdateForm(auth_forms.UserCreationForm):
#     age = forms.IntegerField()

#     # Other fields of `Profile`
