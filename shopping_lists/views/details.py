from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render_to_response
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DetailView
from django.views.generic.edit import DeleteView, FormMixin, FormView
from shopping_lists.models import ShoppingItem, ShoppingList
from shopping_lists.forms import ShoppingItemForm


# Create your views here.


@method_decorator(login_required, name='dispatch')
class DetailsView(SuccessMessageMixin, CreateView):
    form_class = ShoppingItemForm
    template_name = "shopping_lists/shoppinglist_detail.html"
    success_message = "Shopping Item has been created."

    def get_success_url(self):
        return reverse('shopping_lists:details', kwargs={'pk': self.kwargs.get("pk")})

    def form_valid(self, form):
        item_name = form.cleaned_data['name']
        list = ShoppingList.objects.filter(id=self.kwargs.get('pk')).first()
        if ShoppingItem.objects.filter(name=item_name, list=list).exists():
            form._errors[' A Shopping Item with that name already exists'] = ''
            return super(DetailsView, self).form_invalid(form)
        form.instance.list = list
        return super(DetailsView, self).form_valid(form)

    def render_to_response(self, context, **response_kwargs):
        context['shopping_items'] = ShoppingItem.objects.filter(list=self.kwargs.get('pk'))
        context['object'] = ShoppingList.objects.filter(id=self.kwargs.get('pk')).first()
        return super(DetailsView, self).render_to_response(context, **response_kwargs)


@method_decorator(login_required, name='dispatch')
class ShoppingItemUpdate(SuccessMessageMixin, UpdateView):
    model = ShoppingItem
    form_class = ShoppingItemForm
    template_name = "shopping_lists/edit_item_form.html"
    success_message = "Update was successful."

    def get_success_url(self):
        list_id = ShoppingItem.objects.filter(id=self.kwargs.get('pk')).first().list.id
        return reverse('shopping_lists:details', kwargs={'pk': list_id})

    def form_valid(self, form):
        item_name = form.cleaned_data['name']
        list = ShoppingItem.objects.filter(id=self.kwargs.get('pk')).first().list
        item = ShoppingItem.objects.filter(name=item_name, list=list)
        if item.exists() and item.first().id != self.kwargs.get('pk'):
            form._errors[' A Shopping List Item with that name already exists in this List'] = ''
            context = {"form": form}
            context['shopping_items'] = ShoppingItem.objects.filter(list=list)
            return render_to_response("shopping_lists/shoppinglist_detail.html", context=context)
        return super(ShoppingItemUpdate, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class ShoppingItemDelete(SuccessMessageMixin, DeleteView):
    """Deletion of a shopping list."""
    model = ShoppingItem
    template_name = "shopping_lists/delete_item_form.html"
    success_message = "Delete was successful."

    def get_success_url(self):
        list_id = ShoppingItem.objects.filter(id=self.kwargs.get('pk')).first().list.id
        return reverse('shopping_lists:details', kwargs={'pk': list_id})

    def get_context_data(self, **kwargs):
        context = super(ShoppingItemDelete, self).get_context_data(**kwargs)
        context['message'] = self.success_message
        return context