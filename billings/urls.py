from django.urls import path
from . import views

app_name = 'billings'

urlpatterns = [

    path('home/', views.home, name="index"),
    path('invoices/',views.invoices, name="invoices"),
    path('invoice/<int:id>', views.invoice, name="invoice"),
    path('costs/', views.costs, name="costs"),
    path('revenue/', views.revenue, name="revenue"),
    path('expenses/', views.expenses, name="expenses"),
    path('dre/', views.dre, name="dre"),
    path('expenses_cr/', views.expenses_cr, name="expenses_cr"),
] 