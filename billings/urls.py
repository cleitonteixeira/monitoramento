from django.urls import path
from . import views

app_name = 'billings'

urlpatterns = [

    path('', views.home, name="index"),
    path('invoices/',views.invoices, name="invoices"),
    path('invoice/<int:id>', views.invoice, name="invoice"),
    path('costs/', views.costs, name="costs"),
    path('revenue/', views.revenue, name="revenue"),
    
] 