from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from bogis_nails.account.models import Profile

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
            'password1': forms.PasswordInput({'placeholder': 'Password'})
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

class AccountUpdateForm(auth_forms.UserChangeForm):
    birth_date = forms.DateField(required=False)
    profile_picture = forms.ImageField(required=False)
    new_password1 = forms.CharField(label="New Password", strip=False, widget=forms.PasswordInput, required=False)
    new_password2 = forms.CharField(label="Confirm New Password", strip=False, widget=forms.PasswordInput, required=False)

    class Meta:
        model = UserModel
        fields = ('email', 'birth_date', 'profile_picture', 'new_password1', 'new_password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['birth_date'].initial = instance.profile.birth_date
            self.fields['profile_picture'].initial = instance.profile.profile_picture

            
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
        profile.profile_picture = self.cleaned_data['profile_picture']
        new_password = self.cleaned_data['new_password1']
        
        if new_password:
            user.set_password(new_password)
        if commit:
            user.save()
            profile.save()
        return user