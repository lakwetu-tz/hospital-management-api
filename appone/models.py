from django.db import models
# from apptwo.models import Equipment, Payment
from appone.consts import *

    
class Visit(models.Model):
    display_id = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=25, null=True)
    cost = models.PositiveIntegerField()
    suggested_price = models.PositiveIntegerField()
    batch_details = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    subtotal = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    desc = models.TextField(max_length=254, null=True)
    
    def __str__(self):
        return self.display_id

class Branche(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=25, null=True)
    phone = models.CharField(max_length=15, null=True)
    rooms = models.IntegerField()
    location = models.CharField(max_length=50, null=True)
    # equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(verbose_name='name', max_length=50, null=True)
    gender = models.CharField(verbose_name='gender', choices= GENDER, max_length=10, blank=True, null=True)
    d_o_b = models.DateTimeField(verbose_name='Date of Birth', auto_now_add=True)
    phone = models.CharField(verbose_name='phone number', max_length=14, unique=True)
    email = models.EmailField(verbose_name='email', max_length=254, unique=True)
    photo = models.ImageField(verbose_name='image', upload_to=None, height_field=None, width_field=None, blank=True, null=False)
    work_hrs = models.CharField(verbose_name='working hours', null=True, max_length=250)
    # equipment = models.TextField(max_length=50, null=True)
    branch = models.ForeignKey(Branche, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.name)
    
class Patient(models.Model):
    title = models.CharField(choices=TITLE, max_length=10, null=True)
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=15, null=True)
    # photo = models.ImageField(verbose_name='image', upload_to=None, height_field=None, width_field=None,blank=True, null=True)
    # visits = models.ForeignKey(Visit, on_delete=models.CASCADE)
    allargies = models.BooleanField(null=True)
    
    def __str__(self):
        return str(self.name)
    
    
class Queue(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appt = models.BooleanField(null=True)
    time_in = models.TimeField(auto_now_add=True)
    time_out = models.TimeField(auto_now_add=True)
    line = models.IntegerField(choices = LINE, null=True)
    provider = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    status = models.TextField(max_length=20, choices = STATUS_QUEUE, null=True)
    wait_time = models.DurationField(editable=False, null=True)
    
    def __str__(self):
        return str(self.line)
        
    
class Appointment(models.Model):
    title = models.CharField(max_length=20, null=True)
    start_time = models.TimeField(auto_now_add=True, null=True)
    end_time = models.TimeField(auto_now_add=True, null=True)
    desc = models.TextField(max_length=100, blank=True, null=True)
    location = models.TextField(max_length=50, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, null=True)
    
    def __str__(self):
        return str(self.title)
    
class Note(models.Model):
    ref_number = models.DateTimeField(auto_created=True, null=True)
    note_from = models.ForeignKey(Doctor, on_delete=models.PROTECT, null=True)
    note_to = models.ForeignKey(Patient, on_delete=models.PROTECT, null=True)
    subject = models.CharField(max_length=100, null=True)
    body = models.TextField(max_length=500, null=True)
    
    def __str__(self):
        return str(self.ref_number)