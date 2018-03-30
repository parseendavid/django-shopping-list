# from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from .forms import ShoppingListForm

# Create your views here.


@method_decorator(login_required, name='dispatch')
class DashBoardView(CreateView):
    template_name = 'shopping_lists/dashboard.html'
    form_class = ShoppingListForm
    success_url = reverse_lazy("shopping_lists:dashboard")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(DashBoardView, self).form_valid(form)