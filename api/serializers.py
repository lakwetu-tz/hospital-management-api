# from rest_framework.serializers import ModelSerializer 
from rest_framework import serializers
from appone.models import *
from apptwo.models import *

class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        
        
class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        
class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
        
