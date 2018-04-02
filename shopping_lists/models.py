from accounts.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class ShoppingList(models.Model):
    """This is the model for a single shopping list"""
    name = models.CharField(_('list_name'), max_length=20, null=False)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='shopping_lists')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-date_created',)

class ShoppingItem(models.Model):
    """This is the model for a single shopping item in a list"""
    name = models.CharField(_('item_name'), max_length=20, null=False)
    price = models.DecimalField(_('purchase_price(KES'),max_digits=7, decimal_places=2, default=0.00)
    quantity = models.DecimalField(_('item_quantity'),max_digits=7, decimal_places=2, default=0.00)
    list = models.ForeignKey(
        ShoppingList, on_delete=models.CASCADE, related_name='shopping_items')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-date_created',)

