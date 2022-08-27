from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Clinic


def index(request):
   template = loader.get_template("Registration.html")
   return HttpResponse(template.render({}, request))


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

   return HttpResponseRedirect(reverse('index'))


def redirect(request):
   clinic = Clinic.objects.all()[0]
   template = loader.get_template("redirect.html")
   content = {
      'clinic': clinic,
   }

   return HttpResponse(template.render(content, request))

