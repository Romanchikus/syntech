
from django import forms
from .models import *
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.postgres.forms.ranges import DateRangeField, RangeWidget
from datetime import date

default_errors = {
    'required': 'You should select a table',
    'invalid': 'Enter a valid value'
}


class OrderTableForm(forms.Form):

    client_email = forms.EmailField(label='Your email')
    client_name = forms.CharField(
        max_length=254, label='Your name')
    tables = forms.ModelMultipleChoiceField(
        queryset=None, initial=0,
        widget=forms.CheckboxSelectMultiple(),
        error_messages=default_errors)

    def __init__(self, from_date, *args, **kwargs):

        super(OrderTableForm, self).__init__(*args, **kwargs)
        day = date.fromisoformat(from_date)
        self.fields['tables'].queryset = Table.objects.filter(
            date=day, available=True)


class DateCafeForm(forms.Form):

    from_date = forms.DateField(widget=AdminDateWidget())


class DataGenerateForm(forms.Form):

    day_start = forms.DateField(widget=AdminDateWidget())
    day_end = forms.DateField(widget=AdminDateWidget())
