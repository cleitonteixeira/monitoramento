from django.shortcuts import render
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.http import HttpResponse
from datetime import datetime, timedelta
from .models import *
import pandas as pd
import calendar
import random

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
    'labels': ['07/2024', '08/2024', '09/2024','10/2024'],
    'datasets': [
        {
            'label': 'VENDA DE PRODUTOS',
            'data': [random.randint(1000000, 2000000), random.randint(1000000, 2000000), random.randint(1000000, 2000000), random.randint(1000000, 2000000)]
        },
        {
            'label': 'REVENDA DE PRODUTOS',
            'data': [random.randint(10000, 20000), random.randint(10000, 20000), random.randint(10000, 20000), random.randint(10000, 20000)]
        },
        {
            'label': 'VENDA DE SERVICOS',
            'data': [random.randint(50000, 90000), random.randint(50000, 90000), random.randint(50000, 90000),  random.randint(50000, 90000)]
        },
    ]
}
data_costs = [
    ('09/2024', '1000', -6136.73, 'ADMINISTRATIVO'),
    ('09/2024', '1000', -1325.78, 'PESSOAS'),
    ('09/2024', '1100', -57765.95, 'ADMINISTRATIVO'),
    ('09/2024', '1201', -25056.55, 'ADMINISTRATIVO'),
    ('09/2024', '1202', -13430.47, 'ADMINISTRATIVO'),
    ('09/2024', '1202', -85, 'OUTROS'),
    ('09/2024', '1202', -1057.85, 'PESSOAS'),
    ('09/2024', '1203', -474.27, 'ADMINISTRATIVO'),
    ('09/2024', '1203', -15623.15, 'PESSOAS'),
    ('09/2024', '1204', -27997.06, 'ADMINISTRATIVO'),
    ('09/2024', '1204', -34.94, 'OUTROS'),
    ('09/2024', '1204', -4952.28, 'PESSOAS'),
    ('09/2024', '1205', -13757.42, 'ADMINISTRATIVO'),
    ('09/2024', '1205', -20, 'OUTROS'),
    ('09/2024', '1205', -3823.86, 'PESSOAS'),
    ('09/2024', '1206', -3000, 'ADMINISTRATIVO'),
    ('09/2024', '1206', -21.33, 'OUTROS'),
    ('09/2024', '1206', -10599.23, 'PESSOAS'),
    ('09/2024', '1207', -8499.64, 'ADMINISTRATIVO'),
    ('09/2024', '1207', -6681.75, 'PESSOAS'),
    ('09/2024', '1208', -78263.7, 'ADMINISTRATIVO'),
    ('09/2024', '1208', -21671.49, 'PESSOAS'),
    ('09/2024', '1301', -3172.36, 'ADMINISTRATIVO'),
    ('09/2024', '1301', -9119.07, 'PESSOAS'),
    ('09/2024', '1302', -31929.47, 'ADMINISTRATIVO'),
    ('09/2024', '1302', -10166.84, 'PESSOAS'),
    ('09/2024', '1303', -52563.06, 'ADMINISTRATIVO'),
    ('09/2024', '1303', -19236.56, 'PESSOAS'),
    ('09/2024', '1400', -14594.7, 'ADMINISTRATIVO'),
    ('09/2024', '1401', -3112.52, 'ADMINISTRATIVO'),
    ('09/2024', '1401', -94, 'OUTROS'),
    ('09/2024', '1500', -4957.16, 'ADMINISTRATIVO'),
    ('09/2024', '1500', -39.98, 'OUTROS'),
    ('09/2024', '1500', -240, 'PESSOAS'),
    ('09/2024', '1501', -11890.08, 'ADMINISTRATIVO'),
    ('09/2024', '1501', -85, 'OUTROS'),
    ('09/2024', '1501', -7791.58, 'PESSOAS'),
    ('09/2024', '1502', -15031.94, 'ADMINISTRATIVO'),
    ('09/2024', '1502', -528.42, 'PESSOAS'),
    ('09/2024', '9829', -600, 'ADMINISTRATIVO'),
    ('09/2024', '9901', -57.78, 'ADMINISTRATIVO'),
    ('09/2024', '9901', -58518.4, 'INSUMOS'),
    ('09/2024', '9901', -35804.39, 'PESSOAS'),
    ('09/2024', '9903', -18338.17, 'INSUMOS'),
    ('09/2024', '9903', -12676.14, 'PESSOAS'),
    ('09/2024', '9904', -366.73, 'ADMINISTRATIVO'),
    ('09/2024', '9904', -85487.02, 'INSUMOS'),
    ('09/2024', '9904', -84.31, 'OUTROS'),
    ('09/2024', '9904', -43229.55, 'PESSOAS'),
    ('09/2024', '9905', -22675.56, 'INSUMOS'),
    ('09/2024', '9905', -22.75, 'OUTROS'),
    ('09/2024', '9905', -16597.23, 'PESSOAS'),
    ('09/2024', '9906', -163.79, 'ADMINISTRATIVO'),
    ('09/2024', '9906', -81990.96, 'INSUMOS'),
    ('09/2024', '9906', -40295.99, 'PESSOAS'),
    ('09/2024', '9907', -8184, 'ADMINISTRATIVO'),
    ('09/2024', '9907', -32947.26, 'INSUMOS'),
    ('09/2024', '9907', -7.8, 'OUTROS'),
    ('09/2024', '9907', -19016.86, 'PESSOAS'),
    ('09/2024', '9908', -30354.94, 'ADMINISTRATIVO'),
    ('09/2024', '9909', -57035.14, 'ADMINISTRATIVO'),
    ('09/2024', '9909', -88694.34, 'INSUMOS'),
    ('09/2024', '9909', -37036.04, 'PESSOAS'),
    ('09/2024', '9911', -664.02, 'ADMINISTRATIVO'),
    ('09/2024', '9911', -37662.01, 'INSUMOS'),
    ('09/2024', '9911', -21.25, 'OUTROS'),
    ('09/2024', '9911', -17398.16, 'PESSOAS'),
    ('09/2024', '9912', -2871.95, 'ADMINISTRATIVO'),
    ('09/2024', '9912', -33189.24, 'INSUMOS'),
    ('09/2024', '9912', -7.8, 'OUTROS'),
    ('09/2024', '9912', -14472.34, 'PESSOAS'),
    ('09/2024', '9913', -1171.1, 'ADMINISTRATIVO'),
    ('09/2024', '9913', -140485.07, 'INSUMOS'),
    ('09/2024', '9913', -5.08, 'OUTROS'),
    ('09/2024', '9913', -43163.87, 'PESSOAS'),
    ('09/2024', '9915', -2100, 'ADMINISTRATIVO'),
    ('09/2024', '9918', -12542.28, 'ADMINISTRATIVO'),
    ('09/2024', '9918', -135978.34, 'INSUMOS'),
    ('09/2024', '9918', -168.25, 'OUTROS'),
    ('09/2024', '9918', -62748.01, 'PESSOAS'),
    ('09/2024', '9919', -585.36, 'ADMINISTRATIVO'),
    ('09/2024', '9919', -143738.08, 'INSUMOS'),
    ('09/2024', '9919', -38.33, 'OUTROS'),
    ('09/2024', '9919', -92401.35, 'PESSOAS'),
    ('09/2024', '9920', -62.98, 'ADMINISTRATIVO'),
    ('09/2024', '9920', -33876.68, 'INSUMOS'),
    ('09/2024', '9920', -27980.92, 'PESSOAS'),
    ('09/2024', '9921', -23082.62, 'INSUMOS'),
    ('09/2024', '9921', -142.02, 'OUTROS'),
    ('09/2024', '9921', -26051.64, 'PESSOAS'),
    ('09/2024', '9922', -1812.93, 'ADMINISTRATIVO'),
    ('09/2024', '9922', -9254.64, 'INSUMOS'),
    ('09/2024', '9922', -10396.25, 'PESSOAS'),
    ('09/2024', '9927', -2102.76, 'ADMINISTRATIVO'),
    ('09/2024', '9927', -12850.35, 'INSUMOS'),
    ('09/2024', '9927', -17474.34, 'PESSOAS'),
    ('09/2024', '9928', -109698.33, 'ADMINISTRATIVO'),
    ('09/2024', '9928', -196392.43, 'INSUMOS'),
    ('09/2024', '9928', -162.87, 'OUTROS'),
    ('09/2024', '9945', -131062.27, 'ADMINISTRATIVO'),
    ('09/2024', '9945', -25268.47, 'OUTROS'),
    ('09/2024', '9946', -2883.65, 'ADMINISTRATIVO'),
    ('09/2024', '9946', -947.07, 'OUTROS'),
    ('09/2024', '9946', -300, 'PESSOAS'),
    ('09/2024', '9973', -2199.9, 'ADMINISTRATIVO'),
    ('09/2024', '9973', -70.91, 'OUTROS'),
    ('09/2024', '9973', -5209.53, 'PESSOAS'),
    ('09/2024', '9976', -216.14, 'PESSOAS'),
    ('09/2024', '9978', -56863.18, 'ADMINISTRATIVO'),
    ('09/2024', '9978', -79723.42, 'INSUMOS'),
    ('09/2024', '9978', -57.7, 'OUTROS'),
    ('09/2024', '9978', -95773.04, 'PESSOAS'),
    ('09/2024', '9980', -6661.12, 'ADMINISTRATIVO'),
    ('09/2024', '9980', -12701.1, 'INSUMOS'),
    ('09/2024', '9980', -5470.59, 'PESSOAS'),
    ('09/2024', '9986', -48544.66, 'ADMINISTRATIVO'),
    ('09/2024', '9986', -170657.51, 'INSUMOS'),
    ('09/2024', '9986', -129.29, 'OUTROS'),
    ('09/2024', '9986', -63832, 'PESSOAS'),
    ('09/2024', '9990', -8685.04, 'ADMINISTRATIVO'),
    ('09/2024', '9990', -88220.9, 'INSUMOS'),
    ('09/2024', '9990', -30114.87, 'PESSOAS'),
    ('09/2024', '9991', -19662.87, 'ADMINISTRATIVO'),
    ('09/2024', '9991', -41.33, 'OUTROS'),
    ('09/2024', '9994', -3989.85, 'ADMINISTRATIVO'),
    ('09/2024', '9994', -76980.32, 'INSUMOS'),
    ('09/2024', '9994', -333.95, 'OUTROS'),
    ('09/2024', '9994', -40544.01, 'PESSOAS'),
    ('09/2024', '9996', -600, 'ADMINISTRATIVO'),
    ('09/2024', '9996', -51603.37, 'INSUMOS'),
    ('09/2024', '9996', -33810.77, 'PESSOAS'),
    ('09/2024', '9999', -20730.71, 'ADMINISTRATIVO'),
    ('09/2024', '9999', -1920, 'INSUMOS'),
    ('09/2024', '9999', -82.91, 'OUTROS'),
    ('09/2024', '9999', -592.02, 'PESSOAS'),
    ('10/2024', '1000', -14076.89, 'ADMINISTRATIVO'),
    ('10/2024', '1100', -42523.89, 'ADMINISTRATIVO'),
    ('10/2024', '1101', -8170.57, 'ADMINISTRATIVO'),
    ('10/2024', '1101', -3876.06, 'PESSOAS'),
    ('10/2024', '1102', -5105.15, 'ADMINISTRATIVO'),
    ('10/2024', '1102', -7482.66, 'PESSOAS'),
    ('10/2024', '1105', -15021.44, 'ADMINISTRATIVO'),
    ('10/2024', '1106', -24147.78, 'ADMINISTRATIVO'),
    ('10/2024', '1106', -268870.76, 'JUROS/DESPESAS'),
    ('10/2024', '1200', -18099.16, 'ADMINISTRATIVO'),
    ('10/2024', '1201', -27754.11, 'ADMINISTRATIVO'),
    ('10/2024', '1201', -224.58, 'PESSOAS'),
    ('10/2024', '1202', -11839.07, 'ADMINISTRATIVO'),
    ('10/2024', '1202', -1363.9, 'PESSOAS'),
    ('10/2024', '1203', -1697.25, 'ADMINISTRATIVO'),
    ('10/2024', '1203', -15343.39, 'PESSOAS'),
    ('10/2024', '1204', -29820.5, 'ADMINISTRATIVO'),
    ('10/2024', '1204', -4952.28, 'PESSOAS'),
    ('10/2024', '1205', -9742.9, 'ADMINISTRATIVO'),
    ('10/2024', '1205', -4643.73, 'PESSOAS'),
    ('10/2024', '1206', -10274.83, 'PESSOAS'),
    ('10/2024', '1207', -8414.12, 'ADMINISTRATIVO'),
    ('10/2024', '1207', -6681.75, 'PESSOAS'),
    ('10/2024', '1208', -111641.26, 'ADMINISTRATIVO'),
    ('10/2024', '1208', -21795.72, 'PESSOAS'),
    ('10/2024', '1300', -5307.74, 'ADMINISTRATIVO'),
    ('10/2024', '1301', -2558.86, 'ADMINISTRATIVO'),
    ('10/2024', '1301', -9421.7, 'PESSOAS'),
    ('10/2024', '1302', -29985.98, 'ADMINISTRATIVO'),
    ('10/2024', '1302', -7470.84, 'PESSOAS'),
    ('10/2024', '1303', -42090.57, 'ADMINISTRATIVO'),
    ('10/2024', '1303', -17865.84, 'PESSOAS'),
    ('10/2024', '1400', -2955.85, 'ADMINISTRATIVO'),
    ('10/2024', '1401', -25331.46, 'ADMINISTRATIVO'),
    ('10/2024', '1500', -3406.44, 'ADMINISTRATIVO'),
    ('10/2024', '1500', -5404.62, 'PESSOAS'),
    ('10/2024', '1501', -14301.92, 'ADMINISTRATIVO'),
    ('10/2024', '1501', -8619.97, 'PESSOAS'),
    ('10/2024', '1502', -15031.94, 'ADMINISTRATIVO'),
    ('10/2024', '1502', -528.42, 'PESSOAS'),
    ('10/2024', '9901', -372.06, 'ADMINISTRATIVO'),
    ('10/2024', '9901', -2959.53, 'INSUMOS'),
    ('10/2024', '9901', -34344.29, 'PESSOAS'),
    ('10/2024', '9903', -453.18, 'ADMINISTRATIVO'),
    ('10/2024', '9903', -12647.77, 'PESSOAS'),
    ('10/2024', '9904', -1396.93, 'ADMINISTRATIVO'),
    ('10/2024', '9904', -176.14, 'INSUMOS'),
    ('10/2024', '9904', -47684.92, 'PESSOAS'),
    ('10/2024', '9905', -66.93, 'ADMINISTRATIVO'),
    ('10/2024', '9912', -1602.8, 'INSUMOS'),
    ('10/2024', '9912', -12946.66, 'PESSOAS'),
    ('10/2024', '9913', -274.93, 'ADMINISTRATIVO'),
    ('10/2024', '9913', -5138.66, 'INSUMOS'),
    ('10/2024', '9913', -46183.68, 'PESSOAS'),
    ('10/2024', '9915', -2100, 'ADMINISTRATIVO'),
    ('10/2024', '9918', -12234.65, 'ADMINISTRATIVO'),
    ('10/2024', '9918', -9402.56, 'INSUMOS'),
    ('10/2024', '9918', -64283.44, 'PESSOAS'),
    ('10/2024', '9919', -1479.23, 'ADMINISTRATIVO'),
    ('10/2024', '9919', -83100.44, 'PESSOAS'),
    ('10/2024', '9920', -1182.91, 'ADMINISTRATIVO'),
    ('10/2024', '9920', -295.75, 'INSUMOS'),
    ('10/2024', '9920', -29207.55, 'PESSOAS'),
    ('10/2024', '9921', -717.98, 'ADMINISTRATIVO'),
    ('10/2024', '9921', -25424.78, 'PESSOAS'),
    ('10/2024', '9922', -2063.6, 'ADMINISTRATIVO'),
    ('10/2024', '9922', -1230, 'INSUMOS'),
    ('10/2024', '9922', -10729.97, 'PESSOAS'),
    ('10/2024', '9927', -154.96, 'ADMINISTRATIVO'),
    ('10/2024', '9927', -21496.77, 'PESSOAS'),
    ('10/2024', '9928', -126106.38, 'ADMINISTRATIVO'),
    ('10/2024', '9928', -14597.59, 'INSUMOS'),
    ('10/2024', '9928', -125377.09, 'PESSOAS'),
    ('10/2024', '9931', -3300, 'ADMINISTRATIVO'),
    ('10/2024', '9933', -5421.46, 'ADMINISTRATIVO'),
    ('10/2024', '9933', -6840, 'INSUMOS'),
    ('10/2024', '9933', -8068.5, 'PESSOAS'),
    ('10/2024', '9937', -12117.08, 'ADMINISTRATIVO'),
    ('10/2024', '9937', -6153.97, 'INSUMOS'),
    ('10/2024', '9937', -57987.62, 'PESSOAS'),
    ('10/2024', '9938', -5163.86, 'ADMINISTRATIVO'),
    ('10/2024', '9938', -26658.16, 'PESSOAS'),
    ('10/2024', '9944', -2122.81, 'ADMINISTRATIVO'),
    ('10/2024', '9944', -5936.58, 'PESSOAS'),
    ('10/2024', '9945', -106745.39, 'ADMINISTRATIVO'),
    ('10/2024', '9946', -35119.38, 'ADMINISTRATIVO'),
    ('10/2024', '9946', -2420, 'INSUMOS'),
    ('10/2024', '9946', -10298.6, 'PESSOAS'),
    ('10/2024', '9973', -2199.9, 'ADMINISTRATIVO'),
    ('10/2024', '9973', -13523.42, 'PESSOAS'),
    ('10/2024', '9991', -85.77, 'INSUMOS'),
    ('10/2024', '9994', -7772.21, 'ADMINISTRATIVO'),
    ('10/2024', '9994', -2518.77, 'INSUMOS'),
    ('10/2024', '9994', -38344.32, 'PESSOAS'),
    ('10/2024', '9996', -1026.93, 'ADMINISTRATIVO'),
    ('10/2024', '9996', -1566.47, 'INSUMOS'),
    ('10/2024', '9996', -33011.26, 'PESSOAS'),
    ('10/2024', '9999', -41631.78, 'ADMINISTRATIVO'),
    ('10/2024', '9999', -82459.94, 'INSUMOS'),
    ('10/2024', '9999', -563.64, 'PESSOAS')
]

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
    register =ordenar_despesas(register)
    return register

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
        period = datetime.strptime(date, "%Y-%m").strftime("%m/%Y")
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
    month = calcMonth(date).strftime("%Y-%m")
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
        period = datetime.strptime(date, "%Y-%m").strftime("%m/%Y"),
        type = type
    ).values('type').annotate(
        value=-Sum('value'))
    return expense

def getTotalExpensesForBranch(id,date):
    expenses = FinancialTransactions.objects.filter(
        branch__id=id.id,
        period = datetime.strptime(date, "%Y-%m").strftime("%m/%Y")
    ).values('period').annotate(
        value=-Sum('value'))
    return expenses

def getTotalExpensesMonth(id):
    expenses = FinancialTransactions.objects.filter(
        branch__id=id.id
    ).values('period').annotate(
        total=-Sum('value')
    ).order_by('period')[:6]
    return expenses

def getTotalExpensesEnterprise():
    today = datetime.now().strftime('%Y-%m')
    month = calcMonth(today).strftime('%Y-%m')
    data = calcMonth(today).strftime('%m/%Y')
    expenses = FinancialTransactions.objects.filter(
        period=data,
        type__in=['ADMINISTRATIVO','INSUMOS','PESSOAS','OUTROS']
    ).values('period','type').annotate(
        value=-Sum('value')
    )
    tExpenses = []
    for expense in expenses:
        percent = getValueExpensePercentMonth(month,expense['type'])
        exs = {
                'type': expense['type'],
                'value': expense['value'],
                'percent': percent
            }
        tExpenses.append(exs)
    return tExpenses


def getTotalExpensesWithType():
    months = last6Months()
    expenses = FinancialTransactions.objects.filter(period__in=months, type__in=['ADMINISTRATIVO','INSUMOS','PESSOAS','OUTROS']).values('period','type').annotate(
        total=-Sum('value')
    ).order_by('period')
    
    return expenses

def last6Months():
    today = datetime.now()
    months = []
    previous_month = today.replace(day=1) - timedelta(days=1)
    for _ in range(6):
        previous_month -= timedelta(days=30)
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
    return render(request, 'pages/costs.html', context={
        'expenseWithType': getTotalExpensesWithType(),
        'months': last6Months(),
        'resultMonth' : getTotalExpensesEnterprise()
        # 'data_rel' : data_rel,
        # 'revenue_data' : revenue_data,
        # 'input_percent_cost': calc_percent(data_rel['input'][-1],data_rel['input'][-2]),
        # 'staff_expenses_percent_cost': calc_percent(data_rel['staff_expenses'][-1],data_rel['staff_expenses'][-2]),
        # 'administrative_percent_cost': calc_percent(data_rel['administrative'][-1],data_rel['administrative'][-2]),
        # 'taxes_revenue_percent_cost': calc_percent(data_rel['taxes_revenue'][-1],data_rel['taxes_revenue'][-2]),
        # 'revenue_percent': calc_percent(data_rel['revenue_list'][-1],data_rel['revenue_list'][-2]),
        # 'input_cost': data_rel['input'][-1],
        # 'staff_expenses_cost': data_rel['staff_expenses'][-1],
        # 'taxes_revenue_cost': data_rel['taxes_revenue'][-1],
        # 'administrative_cost': data_rel['administrative'][-1],
        # 'revenue_total': data_rel['revenue_list'][-1]
    })

def revenue(request):
    return render(request, 'pages/revenue.html', context={
        'revenue_total': data_rel['revenue_list'][-1],
        'revenue_percent': calc_percent(data_rel['revenue_list'][-1],data_rel['revenue_list'][-2]),
        'revenue_data' : revenue_data,
        'revenue_detail_list' : revenue_detail_list,
    })
    
def dre(request):
    return render(request, 'pages/dre.html',context={
        
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
    