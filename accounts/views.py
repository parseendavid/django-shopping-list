from django.contrib.auth.views import (LoginView, PasswordResetView, PasswordResetConfirmView,
                                       PasswordResetDoneView, PasswordResetCompleteView, LogoutView)
from django.views.generic import CreateView

from .forms import CustomAuthenticationForm, CustomUserCreationForm, CustomSetPasswordForm
from django.urls import reverse_lazy

# Create your views here.


class LoginView(LoginView):
    """Form view for Login"""
    form_class = CustomAuthenticationForm
    template_name = "accounts/login-page.html"
    redirect_authenticated_user = True

class SignUpView(CreateView):
    """Creating a new non-super-user"""
    template_name = "accounts/sign-up-page.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("accounts:login")


class ResetPassword(PasswordResetView):
    """Sends email to user for password reset."""
    email_template_name = 'accounts/emails/password_reset_email.html'
    success_url = reverse_lazy('accounts:reset_done')


class DoneResetPassword(PasswordResetDoneView):
    """Tells user that email for reset has been send reset done."""
    template_name = 'accounts/reset_done.html'


class ConfirmResetPassword(PasswordResetConfirmView):
    """Returns form for changing the password."""
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('accounts:reset_complete')
    template_name = 'accounts/reset_confirm.html'


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    """Notifies User thank password change has been completed successfully"""
    template_name = 'accounts/reset_complete.html'


class CustomLogoutView(LogoutView):
    """Cutomised logout view"""
    next_page = reverse_lazy("home_page")

