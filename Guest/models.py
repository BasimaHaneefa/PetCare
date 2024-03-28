from django.db import models
from Admin.models import tbl_place
# Create your models here.

class tbl_user(models.Model):
    user_name=models.CharField(max_length=50)
    user_address=models.CharField(max_length=50)
    user_cont=models.CharField(max_length=11)
    user_email=models.CharField(max_length=50)
    user_password=models.CharField(max_length=8)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    user_photo=models.FileField( upload_to='UserPhoto/')
    
class tbl_shop(models.Model):
    shop_name=models.CharField(max_length=50)
    shop_address=models.CharField(max_length=50)
    shop_contact=models.CharField(max_length=15)
    shop_email=models.CharField(max_length=50)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    shop_password=models.CharField(max_length=8)
    shop_photo=models.FileField( upload_to='ShopDoc/')
    shop_proof=models.FileField( upload_to='ShopDoc/')
    shop_vstatus=models.CharField(max_length=2, default=0)
    
class tbl_hospital(models.Model):
    hospital_name=models.CharField(max_length=50)
    hospital_address=models.CharField(max_length=50)
    hospital_contact=models.CharField(max_length=15)
    hospital_email=models.CharField(max_length=50)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    hospital_password=models.CharField(max_length=8)
    hospital_logo=models.FileField( upload_to='HospitalDoc/')
    hospital_proof=models.FileField( upload_to='HospitalDoc/')
    hospital_vstatus=models.CharField(max_length=2, default=0)
    
class tbl_petboarding(models.Model):
    boarding_name=models.CharField(max_length=50)
    boarding_address=models.CharField(max_length=50)
    boarding_contact=models.CharField(max_length=15)
    boarding_email=models.CharField(max_length=50)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    boarding_password=models.CharField(max_length=8)
    boarding_logo=models.FileField( upload_to='BoardDoc/')
    boarding_proof=models.FileField( upload_to='BoardDoc/')
    boarding_status=models.CharField(max_length=2, default=0)