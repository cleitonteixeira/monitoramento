from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def home (request):
    bdata = datetime.now()
    data = bdata.strftime("%Y-%m-%d")
    fdata = bdata.strftime("%d/%m/%Y")
    return render(request, 'pages/home.html', context={
        'name': 'Cleiton Santos',
        'company':'Nutribem Refeicoes LTDA',
        'date':data,
        'fdata':fdata
    })

def invoice (request):
    return render(request, 'pages/invoice.html')