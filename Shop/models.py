from django.db import models
from Admin.models import *
from Guest.models import *

# Create your models here.

class tbl_product(models.Model):
    product_name=models.CharField(max_length=50)
    product_rate=models.CharField(max_length=50)
    product_photo=models.FileField(upload_to='ShopDoc/')
    product_details=models.CharField(max_length=400,null=True)
    shop=models.ForeignKey(tbl_shop,on_delete=models.CASCADE)
    subc=models.ForeignKey(tbl_subcategory,on_delete=models.CASCADE)

class tbl_food(models.Model):
    company_name=models.CharField(max_length=50)
    food_rate=models.CharField(max_length=50)
    food_photo=models.FileField(upload_to='ShopDoc/')
    food_content=models.CharField(max_length=50)
    shop=models.ForeignKey(tbl_shop,on_delete=models.CASCADE)
    subc=models.ForeignKey(tbl_subcategory,on_delete=models.CASCADE)
    
class tbl_pet(models.Model):
    pet_dob=models.CharField(max_length=50)
    pet_rate=models.CharField(max_length=50)
    pet_photo=models.FileField(upload_to='ShopDoc/')
    pet_description=models.CharField(max_length=50)
    shop=models.ForeignKey(tbl_shop,on_delete=models.CASCADE)
    breedtype=models.ForeignKey(tbl_breedtype,on_delete=models.CASCADE)


