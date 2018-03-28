from django.urls import path
<<<<<<< HEAD
from .views import (LoginView, SignUpView, ResetPassword, DoneResetPassword, ConfirmResetPassword,
                    CustomPasswordResetCompleteView)
=======
from .views import LoginView, SignUpView
>>>>>>> Feature added functional Signup and Login Pages.

app_name = "accounts"
urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('signup/', SignUpView.as_view(), name="signup"),
<<<<<<< HEAD
    path('reset/', ResetPassword.as_view(), name="reset"),
    path('reset_done/', DoneResetPassword.as_view(), name="reset_done"),
    path('reset/<uidb64>/<token>/', ConfirmResetPassword.as_view(), name="reset_confirm"),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='reset_complete'),
]
=======
]
>>>>>>> Feature added functional Signup and Login Pages.
