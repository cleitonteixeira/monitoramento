from django.urls import path
from billings.views import home,invoice

urlpatterns = [
    
    path('', home),
    path('invoice/',invoice)
]