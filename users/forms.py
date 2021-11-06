from django.contrib.auth import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUserApp
from django import forms
from .models import ManBazu
from django.forms import TextInput, EmailInput, PasswordInput, fields, widgets
from django.utils.translation import gettext_lazy as _


class UserCreateNew(UserCreationForm):
    class Meta:
        model = CustomUserApp
        fields = ('email',)

class UserChangeFormOriginal(UserChangeForm):
    class Meta:
        model = CustomUserApp
        fields = ('email',)

class LoginUserForm(forms.Form):
    class Meta:
        model = ManBazu
        fields = ['email', 'password']
        widgets = {
            'email': EmailInput(attrs={'placeholder': 'email address'})
        }
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'email address'})
        )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'password'})
        )