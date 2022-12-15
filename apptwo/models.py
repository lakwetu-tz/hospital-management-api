from django.db import models
from appone.models import Patient
    
STATUS = [
    (1, 'Waiting For Payment'),
    (2, 'paid'),
]

TRANSACTION_TYPE = [
    ('sales','sales'),
    ('purchases','purchases'),
    ('receipts','receipts'), 
    ('payments','payments')
]
REF = [
    (1, 'Deposit'),
    (2, 'Second Deposit'),
    (3, 'Third Deposit'),
    (4, 'Full Payment'),
]
MODE = [
    (1, 'Cash'),
    (2, 'Check'),
    (3, 'Credit/Debit Card'),
]

class Pro_Serv(models.Model):
    name = models.CharField(max_length=100, verbose_name='name', blank=True, null=True)
    cost_per_unit = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    sell = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    status =  models.TextField(max_length=100, verbose_name='status', blank=True, null=True)
    tag = models.SlugField(max_length=100, verbose_name='tag', blank=True, null=True)
    stock = models.IntegerField(null=True)
    low_stock = models.BooleanField(null=True)
    descr = models.TextField(max_length=100, verbose_name='description', blank=True, null=True)

    def __str__(self):
        return self.name
    
class Equipment(models.Model):
    name = models.CharField(max_length=100, verbose_name='name', blank=True, null=True)
    type = models.CharField(max_length=100, verbose_name='type', blank=True, null=True)
    tag = models.CharField(max_length=100, verbose_name='tag', blank=True, null=True)
    color = models.CharField(verbose_name='color', max_length=50, blank=True, null=True)
    status = models.TextField(max_length=100, verbose_name='status', blank=True, null=True)
    desc = models.TextField(max_length=100, verbose_name='description', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    
class Invoice(models.Model):
    number = models.CharField(max_length=100, null=True)
    ref = models.CharField(max_length=10, blank=True, null=True)
    to = models.ForeignKey(Patient, on_delete=models.PROTECT, null=True)
    date = models.CharField(max_length=20, null=True)
    due = models.CharField(max_length=20, null=True)
    total_amount = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    paid_amount = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    outstanding = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    status = models.IntegerField(choices=STATUS, null=True)
    
    def __str__(self):
        return self.number
    

class Payment(models.Model):
    payment_number = models.PositiveIntegerField()
    transaction_type = models.CharField(choices=TRANSACTION_TYPE, max_length=50, null=True)
    transaction_date = models.CharField(max_length=50, null=True)
    ref = models.IntegerField(choices=REF, default='', null=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    mode = models.IntegerField(choices=MODE, default='')
    amount = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    currency = models.TextField(choices=STATUS, null=True)
    date_created = models.IntegerField(null=True)
    
    def __str__(self):
        return self.payment_number
     