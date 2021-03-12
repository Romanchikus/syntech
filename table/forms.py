
from django import forms
from .models import *


class OrderTableForm(forms.Form):

    client_email = forms.EmailField(label='Your email')
    client_name = forms.CharField(max_length=254, label='Your name')
    tables = forms.ModelMultipleChoiceField(
        queryset=Table.objects.filter(available=True),
        widget=forms.CheckboxSelectMultiple)
