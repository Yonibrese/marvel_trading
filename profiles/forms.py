from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=30, required=False,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=256, help_text='Required',
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(help_text=password_validation.password_validators_help_text_html(),
                                label='Set Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
