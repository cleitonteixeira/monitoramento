from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="index"),
    path('invoices/',views.invoices, name="invoices"),
    path('invoice/<int:id>', views.invoice, name="invoice"),
    path('costs/', views.costs, name="costs")
    
] 