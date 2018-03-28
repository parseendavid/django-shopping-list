"""Forms for our shopping list."""
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import User


class CustomAuthenticationForm(AuthenticationForm):
    """Modified form from auth"""
    username = forms.EmailField(
        max_length=50,
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Email",
            "autocomplete": "email",
            "autofocus": True,
        })

    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password",
                "autocomplete": "password",
            }
        )
    )


class CustomUserCreationForm(UserCreationForm):
    """Modified signup form"""

    email = forms.EmailField(
        max_length=50,
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Your Email...",
            "autocomplete": "email",
            "autofocus": True,
        })

    )
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password",
                "autocomplete": "password",
            }
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password Confirm",
                "autocomplete": "password",
            }
        ),
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ("email",)
