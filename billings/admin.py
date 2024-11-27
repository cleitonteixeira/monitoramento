from django.contrib import admin
from .models import Branch, TypeBranch, FinancialTransactions, FinancialClassification


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