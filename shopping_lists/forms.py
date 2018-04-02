from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import ShoppingList, ShoppingItem


class ShoppingListForm(ModelForm):

    class Meta:
        model = ShoppingList
        fields = ("name",)
        labels = {
            "name":_("Shopping List Name")
        }
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "List Name",
                "autocomplete": "random_name",
            }),
        }

class ShoppingItemForm(ModelForm):

    class Meta:
        model = ShoppingItem
        fields = ("name", "price", "quantity",)
        labels = {
            "name":_("Item Name"),
            "price":_("Price"),
            "quantity":_("Quantity"),
        }
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Item Name",
                "autocomplete": "random_name",
            }),
            "price": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Item Price",
                "autocomplete": "random_name",
            }),
            "quantity": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Item Quantity",
                "autocomplete": "random_name",
            }),
        }
