from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from user.models import UserModel


class RegistrationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2',)


class LoginForm(AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ('email', 'password',)


