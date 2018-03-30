from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import ShoppingList


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
