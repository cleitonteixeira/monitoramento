from django.urls import path
from . import views

urlpatterns = [

    path('', views.home),
    path('invoice/<int:id>',views.invoice)
] 