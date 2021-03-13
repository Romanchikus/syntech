from django.shortcuts import render
from django.views.generic import ListView, FormView
from django.views.generic.edit import BaseUpdateView
from .models import *
from .forms import OrderTableForm, DataCafeForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from datetime import date, timedelta


class HomePageView(ListView):

    model = Table
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["order_form"] = OrderTableForm()
        context["date_form"] = DataCafeForm()
        if self.request.GET.get('from_date', False):
            day = date.fromisoformat(self.request.GET['from_date'])
        else:
            day = date.today()

        context["date_next"] = (day + timedelta(days=1)).isoformat()
        context["date_prev"] = (day - timedelta(days=1)).isoformat()
        return context

    def get_queryset(self):

        if self.request.GET.get('from_date', False):
            return Table.objects.filter(date=self.request.GET['from_date'])
        return super().get_queryset()


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


# class GenerateFakeData():
#     from datetime import datetime
#     names = ['a', 'b', 'c']
#     weights = [12, 15, 23]

#     params = zip(names, weights)
#     products = [ProductVariant(name=param[0], weight=param[1]) for param in params]


#     products = []
#     coordinates = [(1,1),(1,50),(1,100),(50,100),(100,1),(100,50),(100,100)]
#     for coordinate in coordinates:

#         ProductVariant(abscissa=coordinate[0],
#                        ordinate=coordinate[1],
#                        date = datetime(2010, 2, 1)
#                        )

#         abscissa = IntegerRangeField()
#     ordinate = IntegerRangeField()
#     width = IntegerRangeField(default=22)
#     height = IntegerRangeField(default=22)
#     num_of_seats = models.IntegerField(default=2)
#     available = models.BooleanField(default=True)
#     client_name = models.CharField(max_length=254,default='Roman')
#     client_email = models.EmailField(default='13ternopil@gmail.com')
#     date = models.DateField()

#     ProductVariant.objects.bulk_create(products)
