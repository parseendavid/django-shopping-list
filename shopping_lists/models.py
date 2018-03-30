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

