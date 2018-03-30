from django.urls import path

from .views import (ConfirmResetPassword, CustomPasswordResetCompleteView,
                    DoneResetPassword, LoginView, ResetPassword, SignUpView, CustomLogoutView)

app_name = "accounts"
urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('reset/', ResetPassword.as_view(), name="reset"),
    path('reset_done/', DoneResetPassword.as_view(), name="reset_done"),
    path('reset/<uidb64>/<token>/', ConfirmResetPassword.as_view(), name="reset_confirm"),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='reset_complete'),
]
