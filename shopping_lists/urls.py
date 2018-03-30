from django.urls import path

from .views import DashBoardView, ShoppingListUpdate

app_name = "shopping_lists"
urlpatterns = [
    path('list_update/<pk>/', ShoppingListUpdate.as_view(), name='update'),
    path('', DashBoardView.as_view(), name='dashboard'),
]
