from django.db import models
from Guest.models import *

# Create your models here.

class tbl_doctor(models.Model):
    doctor_name=models.CharField(max_length=50)
    doctor_contact=models.CharField(max_length=12)
    doctor_photo=models.FileField( upload_to='HospitalDoc/')
    hospital=models.ForeignKey(tbl_hospital,on_delete=models.CASCADE)


