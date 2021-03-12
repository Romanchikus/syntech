from django.shortcuts import render
from django.views.generic import ListView, FormView
from django.views.generic.edit import BaseUpdateView
from .models import *
from .forms import OrderTableForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect


class HomePageView(ListView):

    model = Table
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["order_form"] = OrderTableForm()
        return context


class OrderTable(HomePageView, FormView):

    form_class = OrderTableForm
    template_name = 'home.html'
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):

        form = OrderTableForm(request.POST)
        
        if not form.is_valid():
            
            view = HomePageView()
            view.setup(request)
            view.object_list = view.get_queryset()
            context = view.get_context_data()
            context["order_form"] = form
            return render(request, 'home.html', context)
            
        return self.form_valid(form)

        

    def form_valid(self, form):
        print(form.cleaned_data['tables'])

        for table in form.cleaned_data['tables']:
            table.client_email = form.cleaned_data['client_email']
            table.client_name = form.cleaned_data['client_name']
            table.available = False
            table.save()

        return super(OrderTable, self).form_valid(form)
