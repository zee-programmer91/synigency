from django.db import models

# Create your models here.
class Clinic(models.Model):
    clinic_name = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    ward_number = models.IntegerField()
    tel_number= models.CharField(max_length=10)
    password = models.CharField(max_length=255)