from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TypeBranch(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.name
    
    
class Branch(models.Model):
    branch_id = models.IntegerField()
    name = models.CharField(max_length=50)
    type = models.ForeignKey(TypeBranch, on_delete=models.SET_NULL, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=14)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Cost(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    period = models.DateField()
    value = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Invoice(models.Model):
    launch_id = models.CharField(max_length=12)
    type = models.CharField(max_length=30)
    value = models.FloatField()
    expiration = models.DateField()
    branch_id = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    supplier_id = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    
class Classification(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

class Dre(models.Model):
    value = models.FloatField()
    period = models.DateField()
    classification_id = models.ForeignKey(Classification, on_delete=models.SET_NULL, null=True)
    branch_id = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
