from django.urls import path, include
from .views import *
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),
    path('order_tables', OrderTable.as_view(), name='order_tables'),
    path('generate_data', GenerateTableData.as_view(), name='generate_tables'),
]