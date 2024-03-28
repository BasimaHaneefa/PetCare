from django.db import models
from Admin.models import *
from Guest.models import *

# Create your models here.

class tbl_gdetails(models.Model):
    gd_photo=models.FileField( upload_to='BoardDoc/')
    gd_details=models.CharField(max_length=100)
    gd_pets=models.CharField(max_length=50)
    grooming=models.ForeignKey(tbl_groomingtype,on_delete=models.CASCADE)
    boarding=models.ForeignKey(tbl_petboarding,on_delete=models.CASCADE)

class tbl_staff(models.Model):
    staff_name=models.CharField(max_length=40)
    staff_address=models.CharField(max_length=60)
    staff_gender=models.CharField(max_length=10,default=0)
    staff_email=models.CharField(max_length=50)
    staff_contact=models.CharField(max_length=15)
    staff_photo=models.FileField( upload_to='BoardDoc/')
    staff_proof=models.FileField( upload_to='BoardDoc/')
    grooming=models.ForeignKey(tbl_groomingtype,on_delete=models.CASCADE)
    boarding=models.ForeignKey(tbl_petboarding,on_delete=models.CASCADE,null=True)
    

class tbl_gallery(models.Model):
    gallery_photo=models.FileField( upload_to='BoardDoc/')
    gallery_caption=models.CharField(max_length=60)
    gd=models.ForeignKey(tbl_gdetails,on_delete=models.CASCADE)