from django.shortcuts import render
from django.db.models import Sum, Q
from django.db.models.functions import TruncMonth
from django.http import HttpResponse
from datetime import datetime, timedelta
from .models import *
import pandas as pd
import calendar
import random

from . import completaBD
from . import completDRE

def ExpenseDataCreate(data):
    print (data)
    register = []
    data_cr = []
    for mesano,cr,valor,descricao in data:
        register_cr = {
            'cr': cr,
            'mesano': mesano,
        }
        data_cr.append(register_cr)
    
    data_cr = pd.DataFrame(data_cr)
    data_cr = data_cr.drop_duplicates(subset=['cr','mesano'])
    data_cr = data_cr.values.tolist()
    for register_cr in data_cr:
        register.append(
                {
                    'cr': register_cr[0],
                    'mesano': register_cr[1],
                    'despesas': [
                        {
                            'ADMINISTRATIVO': 0
                        },{
                            'PESSOAS': 0
                        },{
                            'INSUMOS': 0
                        },{
                            'OUTROS': 0
                        }
                    ],
                }
        )
        
    for mesano,cr,valor,descricao in data:
        atualizar_despesa(register, cr, mesano, descricao, valor)
    register = ordenar_despesas(register)
    return register


def setValuesBD():
    values = completaBD.consulta()
    for value in values:
        print(value)

def ordenar_despesas(despesas):
    return sorted(despesas, key=lambda x: (x['cr']))

def atualizar_despesa(despesas, cr, mesano, tipo_despesa, novo_valor):
    for registro in despesas:
        if registro['cr'] == cr:
            if registro['mesano'] == mesano:
                for despesa in registro['despesas']:
                    if tipo_despesa in despesa:
                        despesa[tipo_despesa] = novo_valor*(-1)
                        return  # Sai do loop se encontrou e atualizou

def getExpenses(id,date):
    tExpenses = []
    expenses = FinancialTransactions.objects.filter(
        branch__id=id.id,
        period = datetime.strptime(date, "%Y-%m").strftime("%m/%Y"),
        type__in=['ADMINISTRATIVO','INSUMOS','PESSOAS']
    )
    for expense in expenses:
        percent = getValueExpensePercent(id,date,expense.type)
        exs = {
                'type': expense.type,
                'value': expense.value*(-1),
                'percent': percent
            }
        tExpenses.append(exs)
    return tExpenses
    
def getBranch(code):
    branch = Branch.objects.get(code=code)
    return branch

def getValueExpensePercent(id,date,type):
    month = calcMonth(date).strftime("%Y-%m")
    lastValue =  getValueEspense(id,month,type).first()
    if lastValue:
        lastValue = lastValue.value
    else:
        lastValue = 0
    atualValue = getValueEspense(id,date,type).first().value
    if lastValue != 0:
        percent = calc_percent(
                atualValue,
                lastValue
            )
    else:
        percent = 0
    return percent

def getValueExpensePercentMonth(date,type):
    print (date.strftime("%Y-%m"))
    month = calcMonth(date.strftime("%Y-%m"))
    print (month)
    lastValue =  getValueExpenseTypeSum(month,type)
    if lastValue:
        lastValue = lastValue
    else:
        lastValue = 0
    atualValue = getValueExpenseTypeSum(date,type)
    if lastValue != 0:
        percent = calc_percent(
                atualValue[0]['value'],
                lastValue[0]['value']
            )
    else:
        percent = 0
    return percent

def getValueEspense(id,date,type):
    expense = FinancialTransactions.objects.filter(
        branch__id=id.id,
        period = datetime.strptime(date, "%Y-%m").strftime("%m/%Y"),
        type = type
    )
    return expense

def getValueExpenseType(date,type):
    expense = FinancialTransactions.objects.filter(
        period = datetime.strptime(date, "%Y-%m").strftime("%m/%Y"),
        type = type
    )
    return expense

def getValueExpenseTypeSum(date,type):
    expense = FinancialTransactions.objects.filter(
        period = date.strftime("%m/%Y"),
        type = type
    ).values('type').annotate(
        value=-Sum('value'))
    return expense

def getTotalExpensesForBranch(id,date):
    expenses = FinancialTransactions.objects.filter(
        branch__id=id.id,
        period = datetime.strptime(date, "%Y-%m").strftime("%m/%Y"),
        type__in=['ADMINISTRATIVO','INSUMOS','PESSOAS']
    ).values('period').annotate(
        value=-Sum('value'))
    return expenses

def getTotalExpensesMonth(id):
    months = last6Months()
    expenses = FinancialTransactions.objects.filter(
        branch__id=id.id,
        period__in=months,
        type__in=['ADMINISTRATIVO','INSUMOS','PESSOAS']
    ).values('period').annotate(
        total=-Sum('value')
    ).order_by('period')[:6]
    return expenses

def getTotalExpensesEnterprise(data):
    today = data.strftime("%m/%Y")
    expenses = FinancialTransactions.objects.filter(
        period=today,
        type__in=['ADMINISTRATIVO','INSUMOS','PESSOAS']
    ).values('period','type').annotate(
        value=-Sum('value')
    )
    tExpenses = []
    
    for expense in expenses:
        percent = getValueExpensePercentMonth(data,expense['type'])
        exs = {
                'type': expense['type'],
                'value': expense['value'],
                'percent': percent
            }
        tExpenses.append(exs)
    return tExpenses

def defExpensesWithMonth(date):
    expenses = FinancialTransactions.objects.filter(
        period = date
    )
    expenses.delete()
    print ("Removidas")
    return expenses

def getTotalExpensesWithType():
    months = last6Months()
    expenses = FinancialTransactions.objects.filter(period__in=months, type__in=['ADMINISTRATIVO','INSUMOS','PESSOAS']).values('period','type').annotate(
        total=-Sum('value')
    ).order_by('period')
    
    return expenses

def last6Months():
    today = datetime.now()
    months = []
    months.append(today.strftime("%m/%Y"))
    previous_month = today.replace(day=1) - timedelta(days=1)
    for _ in range(5):
        previous_month -= timedelta(days=28)
        months.append(previous_month.strftime("%m/%Y"))
    return months[::-1]

def calcMonth(nMonth):
    pMonth = datetime.strptime(nMonth, "%Y-%m")
    lDay = calendar.monthrange(pMonth.year, pMonth.month - 1)[1]
    oneMonth = timedelta(days=lDay)
    pMonth = pMonth - oneMonth
    return pMonth

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
        'data':data,
        'invoices': values
    })

def invoice (request, id):
    return render(request, 'pages/invoice.html')

def costs(request):
    data = calcMonth(datetime.now().strftime("%Y-%m"))    
    if request.POST.get('data') is not None:
        data = datetime.strptime(request.POST.get('data'), '%Y-%m') 
    
    return render(request, 'pages/costs.html', context={
        'expenseWithType': getTotalExpensesWithType(),
        'months': last6Months(),
        'resultMonth' : getTotalExpensesEnterprise(data),
        'data': data
    })

def getTotalRevenueDate(date):
    revenue = FinancialTransactions.objects.filter(
        period = datetime.strptime(date, "%Y-%m").strftime("%m/%Y"),
        type__in=['VENDA DE SERVICOS','VENDA DE PRODUTOS','REVENDA DE PRODUTOS']
    ).values('period').annotate(
        total=Sum('value')
    )
    return revenue

def getPercentRevenue(date):
    lastValue = getTotalRevenueDate(calcMonth(date).strftime("%Y-%m"))
    if lastValue:
        lastValue = lastValue[0]['total']
        atualValue = getTotalRevenueDate(date)
        atualValue = atualValue[0]['total']
        percent = calc_percent(
                atualValue,
                lastValue
            )
    else:
        percent = 0
    return percent

def getRevenueListMonth():
    months = last6Months()
    revenue = FinancialTransactions.objects.filter(
        period__in=months,
        type__in=['VENDA DE SERVICOS','VENDA DE PRODUTOS','REVENDA DE PRODUTOS']
    ).values('period').annotate(
        total=Sum('value')
    ).order_by('period')[:6]
    return revenue

def getRevenueListType():
    months = last6Months()
    revenue = FinancialTransactions.objects.filter(
        period__in=months,
        type__in=['VENDA DE SERVICOS','VENDA DE PRODUTOS','REVENDA DE PRODUTOS']
    ).values('type','period').annotate(
        total=Sum('value')
    )
    return revenue
 
def revenue(request):
    data = calcMonth(datetime.now().strftime("%Y-%m"))
    if request.POST.get('data') is not None:
        data = datetime.strptime(request.POST.get('data'), '%Y-%m')
        return render(request, 'pages/revenue.html',context={
            'revenue': getTotalRevenueDate(request.POST.get('data')),
            'percent': getPercentRevenue(request.POST.get('data')),
            'revenue_list': getRevenueListMonth(),
            'revenue_list_type': getRevenueListType(),
            'months': last6Months(),
            'data': data
        })
    else:
        return render(request, 'pages/revenue.html',context={
            'revenue': getTotalRevenueDate(data.strftime("%Y-%m")),
            'percent': getPercentRevenue(data.strftime("%Y-%m")),
            'revenue_list': getRevenueListMonth(),
            'revenue_list_type': getRevenueListType(),
            'months': last6Months(),
            'data': data
        })

def getItensDRE(date):
    itens =  FinancialTransactions.objects.filter(
        branch__in = Branch.objects.filter(~Q(type__id=1)),
        period = date.strftime("%m/%Y")
    ).values('period','branch__code','type').annotate(
        total=Sum('value')
    ).order_by('branch__code','type')
    return itens
    
def getBranchUsed(date):
    branchs = FinancialTransactions.objects.filter(
        period = date.strftime("%m/%Y"),
        branch__in = Branch.objects.filter(~Q(type__id=1))
    ).values('branch','branch__code').distinct()
    return branchs

def getValuesDRE(date):
    cr = getBranchUsed(date)
    values = []
    for cr in cr:
        value = {
            'branch': cr['branch__code'],
            'Receita_Bruta': completDRE.getRevenueTotalBranch(date,cr['branch__code'])
                if completDRE.getRevenueTotalBranch(date,cr['branch__code']) else [{'branch__code':cr['branch__code']},{'total':'0.00'}],
            'Revenda_de_Mercadorias': completDRE.getRevenueTotalType(date,'REVENDA DE PRODUTOS',cr['branch__code']) 
                if completDRE.getRevenueTotalType(date,'REVENDA DE PRODUTOS',cr['branch__code']) else [{'branch__code':cr['branch__code']},{'total':'0.00'}],
            'Vendas_de_Produtos': completDRE.getRevenueTotalType(date,'VENDA DE PRODUTOS',cr['branch__code'])
                if completDRE.getRevenueTotalType(date,'VENDA DE PRODUTOS',cr['branch__code']) else [{'branch__code':cr['branch__code']},{'total':'0.00'}],
            'Vendas_de_Servicos': completDRE.getRevenueTotalType(date,'VENDA DE SERVICOS',cr['branch__code'])
                if completDRE.getRevenueTotalType(date,'VENDA DE SERVICOS',cr['branch__code']) else [{'branch__code':cr['branch__code']},{'total':'0.00'}],
            'Locacao_de_Bens': completDRE.getRevenueTotalType(date,'LOCACAO DE BENS',cr['branch__code'])
                if completDRE.getRevenueTotalType(date,'LOCACAO DE BENS',cr['branch__code']) else [{'branch__code':cr['branch__code']},{'total':'0.00'}],
            'Provisoes_de_Receitas': completDRE.getRevenueTotalType(date,'PROVISAO DE RECEITAS',cr['branch__code'])
                if completDRE.getRevenueTotalType(date,'PROVISAO DE RECEITAS',cr['branch__code']) else [{'branch__code':cr['branch__code']},{'total':'0.00'}],
        }
        values.append(value)
    return values

def dre(request):
    data = calcMonth(datetime.now().strftime("%Y-%m"))
    if request.POST.get('data') is not None:
        data = datetime.strptime(request.POST.get('data'), '%Y-%m')
        return render(request, 'pages/dre.html',context={
            'crs' : getBranchUsed(data),
            'itens': getItensDRE(data),
            'dre':getValuesDRE(data),
            'data': data
        })
    else:
        return render(request, 'pages/dre.html',context={
            'crs' : getBranchUsed(data),
            'itens': getItensDRE(data),
            'dre':getValuesDRE(data),
            'data': data
        })

def expenses_cr(request):
    if request.POST.get('cr_select') is not None:
        data = datetime.strptime(request.POST.get('data'), '%Y-%m')
        return render(request, 'pages/expenses_cr.html',context={
            'crs' : Branch.objects.all(),
            'cResult': getBranch(request.POST.get('cr_select')),
            'results': getExpenses(getBranch(request.POST.get('cr_select')),request.POST.get('data')),
            'total': getTotalExpensesForBranch(getBranch(request.POST.get('cr_select')),request.POST.get('data')),
            'resultMonth':getTotalExpensesMonth(getBranch(request.POST.get('cr_select'))),
            'data': data
        })
    else:
        return render(request, 'pages/expenses_cr.html',context={
            'crs' : Branch.objects.all()
        })
    
def sincronize(request):
    date = datetime.now()
    if request.POST.get('sinc') == 'sincronizar':
        date = datetime.strptime(request.POST.get('data'), '%Y-%m')
        dados = completaBD.consulta(date.strftime("%m/%Y"))
        defExpensesWithMonth(date.strftime("%m/%Y"))
        for dado in dados:
            saveFinancialTransactions(dado)
    return render(request, 'pages/sincronizar.html', context={
        'crs' : Branch.objects.all(),
        'date': date
    })

def saveFinancialTransactions(data):
    if Branch.objects.filter(code=data[1]).exists():
        branch = Branch.objects.get(code=data[1])
        ftData = FinancialTransactions(
            type = data[3],
            value = data[2],
            period = data[0],
            branch_id = branch.id
        )
        if not FinancialTransactions.objects.filter(type = data[3], period = data[0], branch_id = branch.id).exists():
            ftData.save()
            print("Salvo")
        else:
            print("Ja Existe")
    return




def expenses_type(request):
    if request.POST.get('class_select') is not None:
        data = datetime.strptime(request.POST.get('data'), '%Y-%m')
        print(request.POST.get('class_select'))
        return render(request, 'pages/expense_type.html',context={
            'types' : TypeBranch.objects.all(),
            'cResult': getBranchWithType(request.POST.get('class_select')),
            'results': getExpenses(getBranchWithType(request.POST.get('class_select')),request.POST.get('data')),
            'total': getTotalExpensesForBranch(getBranchWithType(request.POST.get('class_select')),request.POST.get('data')),
            'resultMonth':getTotalExpensesMonth(getBranchWithType(request.POST.get('class_select'))),
            'data': data
        })
    else:
        return render(request, 'pages/expense_type.html',context={
            'types' : TypeBranch.objects.all()
        })
        
def getBranchWithType(id):
    branch = Branch.objects.filter(type__id=id).all()
    return branch