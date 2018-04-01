from django.urls import path

from .views import DashBoardView, ShoppingListUpdate, ShoppingListDelete

app_name = "shopping_lists"
urlpatterns = [
    path('list_update/<pk>/', ShoppingListUpdate.as_view(), name='update'),
    path('list_delete/<pk>/', ShoppingListDelete.as_view(), name='delete'),
    path('', DashBoardView.as_view(), name='dashboard'),
]
