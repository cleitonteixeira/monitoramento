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

input = [
    -1796647.21,-1861382.64,-1823040.44,-1619323.71
]
revenue = [
    3929793.57,4282956.55,5242548.45,4614890.36
]
taxes_revenue = [
    -178616.73,-202299.84,-413851.52,-334747.61
]
administrative = [
    -1219805.09,-903561.46,-1000242.22,-879577.7
]
staff_expenses = [
    -1185820.2,-1059735.99,-1142781.39,-1041888.79
]
months = [
    '06/2024','07/2024','08/2024','09/2024'
]


def calc_percent (last,second_last):
    v_final = last/second_last
    v_final = (v_final-1)*100
    v_final = round(v_final,2)
    return v_final


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
    return render(request, 'pages/costs.html', context={
        'administrative': [administrative * -1 for administrative in administrative],
        'staff_expenses': [staff_expenses * -1 for staff_expenses in staff_expenses],
        'input': [input * -1 for input in input],
        'revenue': revenue,
        'taxes_revenue': [taxes_revenue * -1 for taxes_revenue in taxes_revenue],
        'months': months,
        'input_percent_cost': calc_percent(input[-1],input[-2]),
        'staff_expenses_percent_cost': calc_percent(staff_expenses[-1],staff_expenses[-2]),
        'administrative_percent_cost': calc_percent(administrative[-1],administrative[-2]),
        'taxes_revenue_percent_cost': calc_percent(taxes_revenue[-1],taxes_revenue[-2]),
        'revenue_percent': calc_percent(revenue[-1],revenue[-2]),
        'input_cost': input[-1],
        'staff_expenses_cost': staff_expenses[-1],
        'taxes_revenue_cost': taxes_revenue[-1],
        'administrative_cost': administrative[-1],
        'revenue_total':revenue[-1]
    })