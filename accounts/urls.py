from django.urls import path
from .views import (LoginView, SignUpView, ResetPassword, DoneResetPassword, ConfirmResetPassword,
                    CustomPasswordResetCompleteView)

app_name = "accounts"
urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('reset/', ResetPassword.as_view(), name="reset"),
    path('reset_done/', DoneResetPassword.as_view(), name="reset_done"),
    path('reset/<uidb64>/<token>/', ConfirmResetPassword.as_view(), name="reset_confirm"),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='reset_complete'),
]
