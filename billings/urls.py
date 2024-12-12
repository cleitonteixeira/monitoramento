from django.urls import path
from . import views

app_name = 'billings'

urlpatterns = [
    path("home/", views.home, name="index"),
    path('invoices/',views.invoices, name="invoices"),
    path('invoice/<int:id>', views.invoice, name="invoice"),
    path('costs/', views.costs, name="costs"),
    path('dashboard_faturamento/', views.dashboard_faturamento, name="dashboard_faturamento"),
    path('dashboard_requisicao/', views.dashboard_requisicao, name="dashboard_requisicao"),
    path('dre/', views.dre, name="dre"),
    path('expenses_cr/', views.expenses_cr, name="expenses_cr"),
    path('expenses_type/', views.expenses_type, name="expenses_type"),
    path('sincronize/', views.sincronize, name="sincronize"),
    path('history/', views.history, name="history"),
    path('hora_extra/', views.HoraExtras, name="hora_extra"),
    path('group_events/', views.groupEvents, name="group_events"),
] 