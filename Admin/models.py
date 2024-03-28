from django.db import models

# Create your models here.

class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)

class tbl_category(models.Model):
    category_name=models.CharField(max_length=50)

class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    place_pin=models.CharField(max_length=6)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)

class tbl_subcategory(models.Model):
    sub_name=models.CharField(max_length=50)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)

class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_email=models.CharField(max_length=50)
    admin_cont=models.CharField(max_length=11)
    admin_password=models.CharField(max_length=8)
    
class tbl_breedtype(models.Model):
    breed_name=models.CharField(max_length=50)
    subcategory=models.ForeignKey(tbl_subcategory,on_delete=models.CASCADE)
    
class tbl_groomingtype(models.Model):
    grooming_type=models.CharField(max_length=50)