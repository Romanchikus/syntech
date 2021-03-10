from django.db import models


class Table(models.Model):

    abscissa = models.IntegerField()
    ordinate = models.IntegerField()
    width = models.IntegerField(default=111)
    height = models.IntegerField(default=111)

