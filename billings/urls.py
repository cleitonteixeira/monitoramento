from django.urls import path
from billings.views import home

urlpatterns = [
    path('', home),
]