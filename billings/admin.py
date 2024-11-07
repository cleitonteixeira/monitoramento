from django.contrib import admin
from .models import Branch, TypeBranch


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    ...

@admin.register(TypeBranch)
class TypeBranchAdmin(admin.ModelAdmin):
    ...