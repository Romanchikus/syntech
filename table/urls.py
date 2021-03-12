from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('order_tables', OrderTable.as_view(), name='order_tables'),
]