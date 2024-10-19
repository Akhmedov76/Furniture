from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from accounts.models import UserModel


class RegistrationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2',)


class LoginForm(AuthenticationForm):
    username = None
    email = forms.EmailField(required=True)
