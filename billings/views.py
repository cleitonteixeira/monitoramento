from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def home (request):
    return render(request, 'pages/home.html')

def invoices (request):
    data = datetime.now()
    return render(request, 'pages/invoices.html', context={
        'name': 'Cleiton Santos',
        'company':'Nutribem Refeicoes LTDA',
        'data':data,
        'id_entry': '0000280884',
        'invoice': [
            
        ]
    })

def invoice (request, id):
    return render(request, 'pages/invoice.html')
def graphics (request):
    return render(request, 'pages/graphics.html')