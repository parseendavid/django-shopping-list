from django.urls import path

from .views import DashBoardView

app_name = "shopping_lists"
urlpatterns = [
    path('', DashBoardView.as_view(), name='dashboard')
]
