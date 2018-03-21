from django.urls import path
from .views import login, signup

app_name = "accounts"
urlpatterns = [
    path('login', login, name="login"),
    path('signup', signup, name="signup"),
]