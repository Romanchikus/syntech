from django.shortcuts import render
from django.views.generic import ListView
from .models import *
from .forms import OrderTableForm


class HomePageView(ListView):

    model = Table
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["order_form"] = OrderTableForm()
        return context
