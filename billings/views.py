from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def home (request):
    data = datetime.now()
    data = data.strftime("%Y-%m-%d")
    return render(request, 'pages/home.html', context={
        'name': 'Cleiton Santos',
        'company':'Nutribem Refeicoes LTDA',
        'date':data
    })

def invoice (request):
    return render(request, 'pages/invoice.html')