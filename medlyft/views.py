from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Clinic, Doctor


def add_doctor(request):
    clinic_name = request.GET.get('add_doctor')
    print("clinic name:", clinic_name)
    template = loader.get_template("add_doctor.html")

    clinic = {
        "clinic_names": clinic_name
    }

    content = {
        "clinic": clinic,
    }

    return HttpResponse(template.render(content, request))


def add_patient(request):
    pass


def index(request):
    template = loader.get_template("registration_page.html")
    return HttpResponse(template.render({}, request))


def register_home(request):
    clinic = Clinic.objects.all()[0]
    template = loader.get_template("registration_home.html")
    content = {
        'clinic': clinic,
    }

    return HttpResponse(template.render(content, request))


def registration(request):
    name = request.POST["Name"]
    province = request.POST["Province"]
    region = request.POST["Region"]
    ward = request.POST["Ward"]
    phone = request.POST["Phone"]
    password = request.POST["Password"]

    clinic = Clinic(
        clinic_name=name,
        province=province,
        region=region,
        tel_number=phone,
        password=password,
        ward_number=ward)

    clinic.save()

    return HttpResponseRedirect(reverse('registration_home'))


def save_doctor(request):
    firstname = request.POST['fname']
    lastname = request.POST['lname']
    id_number = request.POST['id']
    registration_number = request.POST['reg_id']
    speciality = request.POST['specializationList']

    docter = Doctor(
        firstname=firstname,
        lastname=lastname,
        id_number=id_number,
        registration_number=registration_number,
        speciality=speciality)

    docter.save()

    return HttpResponseRedirect(reverse('registration_home'))

