from django.contrib import admin
from .models import Branch, TypeBranch, Classification, Dre


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    ...

@admin.register(TypeBranch)
class TypeBranchAdmin(admin.ModelAdmin):
    ...

@admin.register(Classification)
class ClassficationAdmin(admin.ModelAdmin):
    ...
    
@admin.register(Dre)
class DreAdmin(admin.ModelAdmin):
    ...