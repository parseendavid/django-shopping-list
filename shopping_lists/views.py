# from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from shopping_lists.models import ShoppingList
from .forms import ShoppingListForm


# Create your views here.


@method_decorator(login_required, name='dispatch')
class DashBoardView(SuccessMessageMixin, CreateView):
    template_name = 'shopping_lists/dashboard.html'
    form_class = ShoppingListForm
    success_url = reverse_lazy("shopping_lists:dashboard")
    success_message = "Shopping list has been created."

    def render_to_response(self, context, **response_kwargs):
        context['shopping_lists'] = ShoppingList.objects.filter(owner=self.request.user)
        return super(DashBoardView, self).render_to_response(context, **response_kwargs)

    def form_valid(self, form):
        list_name = form.cleaned_data['name']
        owner = self.request.user
        if ShoppingList.objects.filter(name=list_name, owner=owner).exists():
            form._errors['Shopping List already exists'] = ''
            return super(DashBoardView, self).form_invalid(form)
        form.instance.owner = owner
        return super(DashBoardView, self).form_valid(form)
