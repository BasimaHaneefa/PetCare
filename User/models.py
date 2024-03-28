from django.db import models
from Guest.models import tbl_user
from Hospital.models import *
from Shop.models import *
from Petboarding.models import *

# Create your models here.

class tbl_petdetails(models.Model):
    pet_dob=models.CharField(max_length=50)
    breedtype_name=models.CharField(max_length=50)
    pet_weight=models.CharField(max_length=50)
    pet_vaccinedate=models.DateField( null=True)
    pet_details=models.CharField(max_length=100)
    pet_vaccinename=models.CharField(max_length=50)
    pet_photo=models.FileField( upload_to='UserPhoto/')
    pet_gender=models.CharField(max_length=10,default=0)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    
class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=50)
    complaint_content=models.CharField(max_length=50)
    complaint_reply=models.CharField(max_length=50)
    complaint_date=models.DateField(auto_now_add=True)
    complaint_status=models.CharField(max_length=2, default=0)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    
class tbl_feedback(models.Model):
    feedback_content=models.CharField(max_length=50)
    feedback_date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    
class tbl_appointment(models.Model):
    appointment_fordate=models.DateField(max_length=50)
    appointment_fortime=models.CharField(max_length=50)
    appointment_date=models.DateField(auto_now_add=True)
    appointment_status=models.CharField(max_length=2, default=0)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    doctor=models.ForeignKey(tbl_doctor,on_delete=models.CASCADE)
    pet=models.ForeignKey(tbl_petdetails,on_delete=models.CASCADE)
    
class tbl_booking(models.Model):
    booking_date=models.DateField(auto_now_add=True)
    booking_status=models.CharField(max_length=2, default=0)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    payment_status=models.CharField(max_length=2, default=0)
    totalamount=models.CharField(max_length=30,default=0)
    
class tbl_cart(models.Model):
    cart_qty=models.CharField(max_length=50)
    cart_status=models.CharField(max_length=2, default=0)
    food=models.ForeignKey(tbl_food,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE,null=True)
    pet=models.ForeignKey(tbl_pet,on_delete=models.CASCADE,null=True)
    booking=models.ForeignKey(tbl_booking,on_delete=models.CASCADE)
    
class tbl_boardingappointment(models.Model):
    board_fromdate=models.DateField(max_length=50)
    board_todate=models.DateField(max_length=50)
    board_details=models.CharField(max_length=100)
    board_date=models.DateField(auto_now_add=True)
    booking_status=models.CharField(max_length=2, default=0)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    boarding=models.ForeignKey(tbl_petboarding,on_delete=models.CASCADE) 
    
class tbl_groomingappointment(models.Model):
    gappointment_fordate=models.DateField(max_length=50)
    gappointment_date=models.DateField(auto_now_add=True)
    gappointment_status=models.CharField(max_length=2, default=0)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    gd=models.ForeignKey(tbl_gdetails,on_delete=models.CASCADE)
    pet=models.ForeignKey(tbl_petdetails,on_delete=models.CASCADE)
    boarding=models.ForeignKey(tbl_petboarding,on_delete=models.CASCADE,null=True)
    
class tbl_chat(models.Model):
    chat_content = models.CharField(max_length=500)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='ChatFiles/')
    user_from = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_from",null=True)
    user_to = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_to",null=True)
    doctor_from=models.ForeignKey(tbl_doctor,on_delete=models.CASCADE,related_name="doctor_from",null=True)
    doctor_to=models.ForeignKey(tbl_doctor,on_delete=models.CASCADE,related_name="doctor_to",null=True)
    
class tbl_review(models.Model):
    user_rating=models.IntegerField()
    user_review=models.CharField(max_length=20)
    user_name=models.CharField(max_length=20)
    review_datetime=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)
    product= models.ForeignKey(tbl_product,on_delete=models.CASCADE,null=True)
    food=models.ForeignKey(tbl_food,on_delete=models.CASCADE,null=True)
    petboarding=models.ForeignKey(tbl_petboarding,on_delete=models.CASCADE,null=True)
