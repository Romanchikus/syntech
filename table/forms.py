
from django import forms
from django.forms import formset_factory

class OrderTableForm(forms.Form):

    email = forms.EmailField(label='Your email')
    name = forms.CharField(max_length=254, label='Your name')
    number = forms.IntegerField(label='Number of table')
    # num_of_seats = forms.CharField(label='Number of seats')


    def __init__(self, *args, **kwargs):
        super(OrderTableForm, self).__init__(*args, **kwargs)
        self.fields['number'].widget.attrs['readonly'] = True
        # self.fields['num_of_seats'].widget.attrs['readonly'] = True
        
OrderTableFormSet = formset_factory(OrderTableForm, extra = 7)
