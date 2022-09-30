from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-doctor', views.add_doctor, name='add_doctor'),
    path('add-patient', views.add_patient, name='add_patient'),
    path('home', views.home, name='registration_register'),
    path('patientPage', views.patientPage, name='patientPage'),
    path('doctorsPage', views.doctorsPage, name='doctorsPage'),
    path('loginpatient', views.loginpatient, name='loginpatient'),
    path('logindoctor', views.logindoctor, name='logindoctor'),
    path('admin', views.admin, name='admin'),
    path('addminlogin', views.addminlogin, name='addminlogin'),
    path('login', views.login, name='login'),
    path('registration.action', views.registration, name='home.html'),
    path('registration_register', views.registration_register,
         name='registration_register'),
    path('save-doctor', views.save_doctor, name='save_doctor'),
    path('save-patient', views.save_patient, name='save_patient'),
]
