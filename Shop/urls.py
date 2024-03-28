from django.urls import path
from Shop import views

app_name="webshop"

urlpatterns = [
    path('Home/',views.HomePage,name="ShopHome"),
    
    path('Logout/',views.logout,name="Logout"),
    
    path('myprofile/',views.myprofile,name="Profile"),   
    path('Editprofile/',views.editprofile,name="Edit Profile"),
    path('changepass/',views.password,name="Change Password"),
    
    path('ajax_breedtype/',views.ajax_breedtype,name="Ajax_Breedtype"),
    
    
    path('Productdetails/',views.product,name="Product Details"),
    path('delproduct/<int:did>',views.delproduct,name="Delproduct"),
    path('edtproduct/<int:eid>',views.editproduct,name="Edtproduct"),
    
    path('Fooddetails/',views.food,name="Food Details"),
    path('delfood/<int:did>',views.delfood,name="Delfood"),
    
    path('Petdetails/',views.newpet,name="Pet Details"),
    path('delpet/<int:did>',views.delpet,name="Delpet"),
    path('UserBooking/',views.viewbooking,name="User_Booking"),
    path('UserProductBooking/<int:bid>',views.viewuserbooking,name="User Booking"),
    path('PackProduct/<int:packid>',views.packproduct,name="Pack Product"),
    path('ShipProduct/<int:shipid>',views.shipproduct,name="Ship Product"),
    path('DeliveryProduct/<int:outid>',views.outproduct,name="Delivery Product"),
    path('DeliveredProduct/<int:delid>',views.deliproduct,name="Delivered Product"),
]