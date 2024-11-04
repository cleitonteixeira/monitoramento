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
revenue_list = [
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

data_rel = {
    'input' : [ input * -1 for input in input],
    'taxes_revenue' : [taxes_revenue * -1 for taxes_revenue in taxes_revenue],
    'administrative' : [ administrative * -1 for administrative in administrative],
    'staff_expenses' : [ staff_expenses * -1 for staff_expenses in staff_expenses],
    'revenue_list' : [ revenue_list for revenue_list in revenue_list],
    'months' : [months for months in months]
}

revenue_data = {
    'taxes_revenue' : [taxes_revenue * -1 for taxes_revenue in taxes_revenue],
    'revenue_list' : [ revenue_list for revenue_list in revenue_list],
    'months' : [months for months in months]
}
revenue_months = {
    'months' : [months for months in months]
}

revenue_detail_list = {
    'labels': ['07/2024', '08/2024', '09/2024'],
    'datasets': [
        {
            'label': '9901',
            'data': [79661.5, 231278.93, 152390.59]
        },
        {
            'label': '9903',
            'data': [68865.67, 37113.67, 36754.17]
        },
        {
            'label': '9904',
            'data': [218584.96, 268957.46, 178319.66]
        },
        {
            'label': '9905',
            'data': [88453.74, 81653.82, 47050.22]
        },
        {
            'label': '9906',
            'data': [150792.44, 405794.73, 162277.56]
        },
    ]
}

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
        'data_rel' : data_rel,
        'revenue_data' : revenue_data,
        'input_percent_cost': calc_percent(data_rel['input'][-1],data_rel['input'][-2]),
        'staff_expenses_percent_cost': calc_percent(data_rel['staff_expenses'][-1],data_rel['staff_expenses'][-2]),
        'administrative_percent_cost': calc_percent(data_rel['administrative'][-1],data_rel['administrative'][-2]),
        'taxes_revenue_percent_cost': calc_percent(data_rel['taxes_revenue'][-1],data_rel['taxes_revenue'][-2]),
        'revenue_percent': calc_percent(data_rel['revenue_list'][-1],data_rel['revenue_list'][-2]),
        'input_cost': data_rel['input'][-1],
        'staff_expenses_cost': data_rel['staff_expenses'][-1],
        'taxes_revenue_cost': data_rel['taxes_revenue'][-1],
        'administrative_cost': data_rel['administrative'][-1],
        'revenue_total': data_rel['revenue_list'][-1]
    })

def revenue(request):
    return render(request, 'pages/revenue.html', context={
        'revenue_total': data_rel['revenue_list'][-1],
        'revenue_percent': calc_percent(data_rel['revenue_list'][-1],data_rel['revenue_list'][-2]),
        'revenue_data' : revenue_data,
        'revenue_detail_list' : revenue_detail_list,
    })
def expenses(request):
    return render(request, 'pages/expenses.html')