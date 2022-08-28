from django.db import models


class Clinic(models.Model):
    clinic_name = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    ward_number = models.IntegerField()
    tel_number = models.CharField(max_length=10)
    password = models.CharField(max_length=255)


class Doctor(models.Model):
    firstname = models.CharField(max_length=225)
    lastname = models.CharField(max_length=225)
    id_number = models.CharField(max_length=13)
    registration_number = models.IntegerField()
    speciality = models.CharField(max_length=225)

class Patient(models.Model):
    firstname = models.CharField(max_length=225)
    lastname = models.CharField(max_length=225)
    IDnumber = models.CharField(max_length=13)
    FolderNumber = models.IntegerField()
    phone = models.IntegerField()
    Email = models.CharField(max_length=225)
    address1 = models.CharField(max_length=255)



