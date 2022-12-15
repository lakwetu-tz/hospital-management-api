from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from appone.models import *
from appone.models import *
from rest_framework import status

@api_view(['GET'])
def getRoutes(request, format=None):
    routes = {
        'admin':'/api/admin/',
        'doctors':'/api/doctors/',
        'doctor':'/api/doctors/id=id',
        'doctor':'/api/doctors/id=id',
        'doctor':'/api/doctors/id=id',
        'doctor':'/api/doctors/id=id',
        'doctor':'/api/doctors/id=id',
        
        
    }
    return Response(routes)

@api_view(['GET', 'POST', 'DELETE'])
def doctors_list(request, format=None):
    
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        serializer = DoctorsSerializer(doctors, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DoctorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Doctor is added'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        count = Doctor.objects.get().delete()
        return Response({'message': '{} Doctor were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'PUT', 'DELETE'])
def doctors_details(request, id, format=None):
    try:
        doctor = Doctor.objects.get(id=id)
    except Doctor.DoesNotExist:
        return Response({'message':'Doctor does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET':
        serializer = DoctorsSerializer(doctor, many=False)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = DoctorsSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    elif request.method == 'DELETE': 
        doctor.delete() 
        return Response({'message': 'Doctor was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    
    
@api_view(['GET', 'POST', 'DELETE'])   
def patients_list(request, format=None):
    if request.method == 'GET':
        patient = Patient.objects.all()
        serializer = PatientsSerializer(patient, many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = PatientsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Patient is added'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        count = Patient.objects.get().delete()
        return Response({'message': '{} Patient were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def patients_details(request, id, format=None):
    try:
        patient = Patient.objects.get(id=id)
    except Patient.DoesNotExist:
        return Response({'message':'Patient does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET':
        serializer = PatientsSerializer(patient, many=False)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PatientsSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    elif request.method == 'DELETE': 
        patient.delete() 
        return Response({'message': 'Patient was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST', 'DELETE', 'PUT'])   
def notes_list(request, format=None,):
    try:
        note = Note.objects.all()
    except Note.DoesNotExist:
        return Response({'message':'Note does not exist'}, status=status.HTTP_NOT_FOUND) 
    
    if request.method == 'GET':
        serializer = NotesSerializer(note, many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = NotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Notes is added'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        serializer = NotesSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Note.objects.all().delete()
        return Response({'message': '{} Note were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    
 