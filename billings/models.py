from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Branch(models.Model):
    branch_id = models.IntegerField()
    name = models.CharField(max_length=50)

class Supplier(models.Model):
    name = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=14)

class Cost(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    period = models.DateField()
    value = models.FloatField()
    
class Invoice(models.Model):
    launch_id = models.CharField(max_length=12)
    type = models.CharField(max_length=30)
    value = models.FloatField()
    expiration = models.DateField()
    branch_id = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    supplier_id = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)