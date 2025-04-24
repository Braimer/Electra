#forms, register and login , no need to use django default auth forms

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

# Custom Register Form
class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'class': 'input-class', 'placeholder': 'Username'})
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'input-class', 'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'input-class', 'placeholder': 'Confirm Password'})
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# Custom Login Form
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'class': 'input-class', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'input-class', 'placeholder': 'Password'})
    )
