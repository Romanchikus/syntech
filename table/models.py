from django.db import models


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=1, max_value=100, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)



class Table(models.Model):

    
    abscissa = IntegerRangeField()
    ordinate = IntegerRangeField()
    width = IntegerRangeField(default=22)
    height = IntegerRangeField(default=22)
    num_of_seats = models.IntegerField(default=2)
    available = models.BooleanField(default=True)
    client_name = models.CharField(max_length=254,default='Roman')
    client_email = models.EmailField(default='13ternopil@gmail.com')
    date = models.DateField()

    def __str__(self):
        return f"Table №{self.id}"


    
