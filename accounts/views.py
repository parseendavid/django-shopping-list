from django.contrib.auth.views import LoginView
from django.views.generic import FormView, CreateView

from  .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.urls import reverse_lazy

# Create your views here.


class LoginView(LoginView):
    """Form view for Login"""
    form_class = CustomAuthenticationForm
    template_name = "accounts/login-page.html"


class SignUpView(CreateView):
    """Creating a new non-super-user"""
    template_name = "accounts/sign-up-page.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("accounts:login")
