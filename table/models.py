from django.db import models


class Table(models.Model):

    hall = models.ForeignKey('Hall', on_delete=models.CASCADE)
    abscissa = models.IntegerField()
    ordinate = models.IntegerField()
    width = models.IntegerField(default=111)
    height = models.IntegerField(default=111)
    num_of_seats = models.IntegerField()
    available = models.BooleanField(default=True)
    client_name = models.CharField(max_length=254)
    client_email = models.EmailField()


class Hall(models.Model):

    date = models.DateField()
