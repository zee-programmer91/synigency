from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clinic/add_doctor', views.add_doctor, name='add_doctor'),
    path('clinic/save_doctor', views.save_doctor, name='save_doctor'),
    path('clinic/add_patient', views.add_patient, name='add_patient'),
    path('clinic/save_patient', views.save_patient, name='save_patient'),
    path('registration/', views.registration, name='registration_page'),
    path('clinic/home', views.register_home, name='registration_home'),
]
