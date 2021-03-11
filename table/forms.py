
from django import forms
from .models import *


class OrderTableForm(forms.ModelForm):

    class Meta:

        model = Table
        fields = ['client_name', 'client_email']

    client_email = forms.EmailField(label='Your email')
    client_name = forms.CharField(max_length=254, label='Your name')
    number = forms.IntegerField(label='Number of table')
    tables = forms.ModelMultipleChoiceField(
        queryset=Table.objects.filter(available=True),
        widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        super(OrderTableForm, self).__init__(*args, **kwargs)
        self.fields['number'].widget.attrs['readonly'] = True
