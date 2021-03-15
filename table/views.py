from django.shortcuts import render
from django.views.generic import ListView, FormView
from django.views.generic.edit import BaseUpdateView
from .models import *
from .forms import *
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from datetime import date, timedelta
from django.contrib import messages
from cafe.settings import EMAIL_HOST_USER, CAFE_NAME
from django.core.mail import send_mail


class HomePageView(ListView):

    model = Table
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["date_form"] = DateCafeForm()

        if self.request.GET.get("from_date", False):
            context["order_form"] = OrderTableForm(
                from_date=self.request.GET["from_date"]
            )
            day = date.fromisoformat(self.request.GET["from_date"])
        else:
            day = date.today()
            context["order_form"] = OrderTableForm(from_date=day.isoformat())

        context["from_date"] = day.isoformat()
        context["date_next"] = (day + timedelta(days=1)).isoformat()
        context["date_prev"] = (day - timedelta(days=1)).isoformat()
        return context

    def get_queryset(self):

        if self.request.GET.get("from_date", False):
            return Table.objects.filter(date=self.request.GET["from_date"])
        else:
            return Table.objects.filter(date=date.today())


class OrderTable(HomePageView, FormView):

    form_class = OrderTableForm
    success_url = reverse_lazy("home")

    def post(self, request, *args, **kwargs):

        if self.request.POST.get("from_date", False):
            form = OrderTableForm(self.request.POST["from_date"], request.POST)
            day = date.fromisoformat(self.request.POST["from_date"])
        else:
            day = date.today()
            form = OrderTableForm(day.isoformat(), request.POST)

        if not form.is_valid():

            view = HomePageView()
            view.setup(request)
            view.object_list = view.get_queryset()
            context = view.get_context_data()
            context["order_form"] = form
            return render(request, "home.html", context)

        return self.form_valid(form)

    def form_valid(self, form):

        for table in form.cleaned_data["tables"]:
            table.client_email = form.cleaned_data["client_email"]
            table.client_name = form.cleaned_data["client_name"]
            table.available = False
            table.save()

        tables = [i.number for i in form.cleaned_data["tables"]]
        if len(tables) > 1:
            tables = ",".join(map(str, tables))
            message = (
                f"Dear {form.cleaned_data['client_name']} you ordered {tables}"
                f" tables  in '{CAFE_NAME}' cafe for date: {form.cleaned_data['tables'][0].date}"
            )
        else:
            message = (
                f"Dear {form.cleaned_data['client_name']} you ordered {tables[0]}"
                f" table  in '{CAFE_NAME}' cafe for date: {form.cleaned_data['tables'][0].date}"
            )

        subject = f"Order table in '{CAFE_NAME}' cafe"

        recepient = str(form.cleaned_data["client_email"])
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)

        return super(OrderTable, self).form_valid(form)


class GenerateTableData(FormView):

    template_name = "generate_data.html"
    form_class = DataGenerateForm

    def post(self, request, *args, **kwargs):

        form = DataGenerateForm(request.POST)

        if not form.is_valid():
            return self.form_invalid(form)

        self.day_start, self.day_end = self.get_date(request)

        tables = self.generate_tables_list(
            coordinates=request.GET.get("coordinates", False)
        )

        Table.objects.bulk_create(tables)

        messages.add_message(
            request,
            messages.INFO,
            f"Generated tables from {self.day_start} to {self.day_end}",
        )
        print("success")

        return HttpResponseRedirect(reverse("home"))

    def get_date(self, request):

        if request.POST.get("day_start", False):
            day_start = date.fromisoformat(request.POST["day_start"])

            if not request.POST.get("day_end", False):
                day_end = day_start + timedelta(weeks=4)

        if request.POST.get("day_end", False):
            day_end = date.fromisoformat(request.POST["day_end"])

            if not request.POST.get("day_start", False):
                day_start = day_end - timedelta(weeks=4)

        return day_start, day_end

    def generate_tables_list(self, coordinates=False):

        if not coordinates:
            coordinates = [
                (1, 1),
                (1, 50),
                (1, 100),
                (50, 100),
                (100, 1),
                (100, 50),
                (100, 100),
            ]

        tables = list()
        delta = timedelta(days=1)
        day_in_progr = self.day_start
        while day_in_progr <= self.day_end:

            for i in range(len(coordinates)):

                table = Table(
                    abscissa=coordinates[i][0],
                    ordinate=coordinates[i][1],
                    date=day_in_progr,
                    number=i + 1,
                )
                tables.append(table)

            day_in_progr += delta

        return tables
