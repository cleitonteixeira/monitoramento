from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TypeBranch(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return f"{self.id} - {self.name}"
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'tipos de filiais'
        verbose_name = 'tipo de filial'
    
class Branch(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    type = models.ForeignKey(TypeBranch, on_delete=models.SET_NULL, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return f"{self.code} - {self.name} - {self.type.name}"
    
    class Meta:
        ordering = ['code']
        verbose_name_plural = 'filiais'
        verbose_name = 'filial'

class Supplier(models.Model):
    code = models.CharField(max_length=20, unique=True, null=True)
    name = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=14, unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return f"{self.code} - {self.name} - {self.cnpj}"
    
    class Meta:
        ordering = ['cnpj']
        verbose_name_plural = 'fornecedores'
        verbose_name = 'fornecedor'

class Invoice(models.Model):
    launch_id = models.CharField(max_length=12)
    type = models.CharField(max_length=30)
    value = models.FloatField()
    expiration = models.DateField()
    branch_id = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return f"{self.branch.code} - {self.supplier.name} - {self.type} - {self.value}"
    
    class Meta:
        ordering = ['launch_id']
        verbose_name_plural = 'notas fiscais'
        verbose_name = 'nota fiscal'

class FinancialTransactions(models.Model):
    type = models.CharField(max_length=30)
    value = models.FloatField()
    period = models.CharField(max_length=7)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return f"{self.branch.code} - {self.period} - {self.type} - {self.value}"
    
    class Meta:
        ordering = ['period','branch']
        verbose_name_plural = 'transações financeiras'
        verbose_name = 'transação financeira'

class FinancialClassification(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

class Cooperators(models.Model):
    name = models.CharField("Nome",max_length=50)
    cpf = models.CharField("CPF",max_length=11)
    admission = models.DateField("Admissão")
    ocupation = models.CharField("Cargo",max_length=50)
    birthdate = models.DateField("Data de nascimento")
    cod = models.IntegerField("Matrícula",unique=True)
    link = models.IntegerField("Vínculo",unique=True)
    type = models.CharField("Tipo de Contrato",max_length=30)
    sex = models.CharField("Sexo",max_length=30,null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, verbose_name="Filial")
    demission = models.DateField("Demissão",null=True)
    situation = models.CharField("Sitaução Funcional",max_length=30)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return f"{self.cod} - {self.name} - {self.cpf} - {self.ocupation} - {self.admission}"
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'colaboradores'
        verbose_name = 'colaborador'
    
class Events(models.Model):
    cod = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    typeEvent = models.CharField(max_length=30)
    demonstrative = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['cod']
        verbose_name_plural = 'eventos'
        verbose_name = 'evento'

class EventHistory(models.Model):
    cooperator = models.ForeignKey(Cooperators, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    movement = models.CharField(max_length=30,null=True)
    occurrence = models.DateField(null=True)
    competence = models.DateField()
    valuereference = models.FloatField()
    value = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return f"{self.cooperator.cod}- {self.cooperator.name}- {self.competence} - {self.event.cod} - {self.event.name}"
    
    class Meta:
        ordering = ['competence','cooperator','event']
        verbose_name_plural = 'histórico de eventos'
        verbose_name = 'histórico de evento'

class GroupEvents(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'grupos de eventos'
        verbose_name = 'grupo de eventos'

class EventsByGroup(models.Model):
    group = models.ForeignKey(GroupEvents, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.SET_NULL, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return f"{self.id}"
    
    class Meta:
        ordering = ['group','event']
        verbose_name_plural = 'eventos por grupos'
        verbose_name = 'evento por grupo'