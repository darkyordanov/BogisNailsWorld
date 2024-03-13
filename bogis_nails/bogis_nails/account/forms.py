from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class AccountUserChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = UserModel
        fields = '__all__'
        # we can add additional custom fields to the form
        # fields = auth_forms.UserChangeForm.Meta.fields + ('birth_date',)
        

class AccountRegisterForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')
        # fields = auth_forms.UserChangeForm.Meta.fields + ('birth_date',)
        
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            # 'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
            # 'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
            # 'birth_date': forms.DateInput(attrs={'placeholder': 'Birth date'}),
        }

# Update form when user is success register to update her/his profile information later
# class AccountUpdateForm(auth_forms.UserCreationForm):
#     age = forms.IntegerField()

#     # Other fields of `Profile`

#     class Meta(auth_forms.UserCreationForm.Meta):
#         model = UserModel
#         fields = (UserModel.USERNAME_FIELD,)
#         # fields = auth_forms.UserCreationForm.Meta.fields + ("age",)

#     def save(self, commit=True):
#         user = super().save(commit=commit)

#         profile = Profile(
#             user=user,
#             age=self.cleaned_data["age"],
#         )

#         if commit:
#             profile.save()

#         return user