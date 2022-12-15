from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.getRoutes),
    path('api/v1/doctors/', views.doctors_list),
    path('api/v1/doctors/<int:id>', views.doctors_details),
    path('api/v1/patients/', views.patients_list),
    path('api/v1/patients/<int:id>', views.patients_details),
    path('api/v1/notes/', views.notes_list)
    
]
 
urlpatterns = format_suffix_patterns(urlpatterns)