from django.contrib import admin
from .models import *


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    ...

@admin.register(TypeBranch)
class TypeBranchAdmin(admin.ModelAdmin):
    ...

@admin.register(FinancialClassification)
class FinancialClassificationAdmin(admin.ModelAdmin):
    ...
    
@admin.register(FinancialTransactions)
class FinancialTransactionsAdmin(admin.ModelAdmin):
    ...
    
@admin.register(Cooperators)
class CooperatorsAdmin(admin.ModelAdmin):
    ...

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    ...
    
@admin.register(EventHistory)
class EventHistoryAdmin(admin.ModelAdmin):
    ...