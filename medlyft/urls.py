from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-doctor', views.add_doctor, name='add_doctor'),
    path('add-patient', views.add_patient, name='add_patient'),
    path('home', views.register_home, name='registration_home'),
    path('login', views.login, name='login'),
    path('registration.action', views.registration, name='registration_register'),
    path('registration', views.registration_register, name='registration_register'),
    path('save-doctor', views.save_doctor, name='save_doctor'),
    path('save-patient', views.save_patient, name='save_patient'),
]
