from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class HomePageView(ListView):

    model = Table
    template_name = 'home.html'


