"""Forms for our shopping list."""
from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm, PasswordResetForm,
                                       SetPasswordForm)
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import User


class CustomPasswordResetForm(PasswordResetForm):
    """Extension to current auth password reset form"""
    email = forms.EmailField(
        max_length=50,
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Your Email...",
        })

    )
    use_https = True


class CustomAuthenticationForm(AuthenticationForm):
    """Modified form from auth"""
    reset_password = CustomPasswordResetForm
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


class CustomSetPasswordForm(SetPasswordForm):
    """Customised set password form for css magic.."""
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "New Password",
                "autocomplete": "none",
            }
        ),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "New password confirmation",
                "autocomplete": "password",
            }
        )
    )
