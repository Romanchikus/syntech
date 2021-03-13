
from django import forms
from .models import *
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.postgres.forms.ranges import DateRangeField, RangeWidget


class OrderTableForm(forms.Form):

    client_email = forms.EmailField(label='Your email')
    client_name = forms.CharField(max_length=254, label='Your name')
    tables = forms.ModelMultipleChoiceField(
        queryset=Table.objects.filter(available=True),
        widget=forms.CheckboxSelectMultiple)


class DataCafeForm(forms.Form):

    from_date = forms.DateField(widget=AdminDateWidget())
