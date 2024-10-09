from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

values = [
            {'id_entry':'1512','branch':{'branch_id':'9980','name':'Formosa'},'name':'HubTel','value':'259.9','type':'Internet','expiration':datetime.strptime('2024-10-18','%Y-%m-%d')},
            {'id_entry':'1513','branch':{'branch_id':'9999','name':'CD Paracatu'},'name':'Mart Minas Distribuição','value':'17598.55','type':'Insumos','expiration':datetime.strptime('2024-10-18','%Y-%m-%d')},
            {'id_entry':'1514','branch':{'branch_id':'9994','name':'ArcelorMittal Bom Sucesso'},'name':'Leonardo Nunes Oliveira','value':'21590.55','type':'Insumos','expiration':datetime.strptime('2024-10-18','%Y-%m-%d')},
            {'id_entry':'1515','branch':{'branch_id':'9996','name':'USINA VPA'},'name':'MarFirsh','value':'11598.55','type':'Insumos','expiration':datetime.strptime('2024-10-18','%Y-%m-%d')},
        ]

def home (request):
    return render(request, 'pages/home.html', context={
        'invoices': values
    })

def invoices (request):
    data = datetime.now()
    return render(request, 'pages/invoices.html', context={
        'name': 'Cleiton Santos',
        'company':'Nutribem Refeicoes LTDA',
        'data':data,
        'invoices': values
    })

def invoice (request, id):
    return render(request, 'pages/invoice.html')

def costs(request):
    return render(request, 'pages/costs.html')