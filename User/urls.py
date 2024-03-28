from django.urls import path
from User import views

app_name="webuser"

urlpatterns = [
    path('Home/',views.HomePage,name="UserHome"),
    
    path('Logout/',views.logout,name="Logout"),
    
    path('myprofile/',views.myprofile,name="My Profile"),
    
    path('Editprofile/',views.editprofile,name="Edit Profile"),
    
    path('changepass/',views.password,name="Change Password"),
    
    path('Petdetails/',views.petdetails,name="Pet Details"),
    path('delpet/<int:did>',views.delpet,name="Delpet"),
    path('edtpet/<int:eid>',views.edtpet,name="Edtpet"),
    
    path('Complaint/',views.complaint,name="Complaint"),
    path('delcomplaint/<int:did>',views.delc,name="Delc"),
    path('edtcomplaint/<int:eid>',views.edtc,name="Edtc"),
    
    path('Feedback/',views.feedback,name="Feedback"),
    path('delfeedback/<int:did>',views.delf,name="Delf"),
    path('edtfeedback/<int:eid>',views.edtf,name="Edtf"),
    
    path('SearchHospital/',views.searchHos,name="Search Hospital"),
    path('ajax_search/',views.ajax_search,name="Ajax_Search"),
    path('ViewDoctor/<int:vid>',views.viewdoctor,name="View Doctor"), 
    
    path('Appointment/<int:appid>',views.appointment,name="Hospital Appointment"),
    path('ViewAppointment/',views.viewappointment,name="View Appointment"),
    path('CancelAppointment/<int:cid>',views.cancelappointment,name="Cancel"),
    
    path('SearchProduct/',views.searchProduct,name="Search Product"),
    path('ajax_product/',views.ajax_product,name="Ajax_Product"),
    path('BuyProduct/<int:pid>',views.buyproduct,name="Buyproduct"),
    
    path('SearchFood/',views.searchfood,name="Search Food"),
    path('ajax_food/',views.ajax_food,name="Ajax_Food"),
    path('Buyfood/<int:fid>',views.buyfood,name="Buyfood"),
    
    path('SearchPet/',views.searchpet,name="Search Pet"),
    path('ajax_pet/',views.ajax_pet,name="Ajax_Pet"),
    path('Buypet/<int:petid>',views.buypet,name="Buypet"),
    
    path('MyCart/',views.Mycart,name="Cart"),
    path('delcart/<int:did>',views.DelCart,name="delcart"),
    path('cartqty/',views.CartQty,name="cartqty"),
    path('payment/',views.Payment,name="Payment"),
    
    path('MyBooking/',views.viewbooking,name="My Booking"),
    path('CancelBooking/<int:cartid>',views.cancelbooking,name="Cancel Booking"),
    
    path('SearchBoarding/',views.searchboard,name="Search Boarding"),
    path('ajax_boarding/',views.ajax_board,name="Ajax_Board"),
    path('ViewGrooming/<int:vid>',views.viewgrooming,name="View Grooming"), 
    
    path('BoardingAppointment/<int:boardid>',views.bappointment,name="Boarding Appointment"),
    path('ViewBoardingAppointment/',views.viewbappointment,name="View Boarding Appointment"),
    
    path('ViewGallery/<int:gaid>',views.viewgallery,name="View Gallery"),
    
    path('GroomingAppointment/<int:appid>',views.gappointment,name="Grooming Appointment"),
    path('ViewGroomAppointment/',views.viewgappointment,name="View Grooming Appointment"),
  
    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),
    path('rating/<str:cid>',views.rating,name="rating"),
    path('ajaxrating',views.ajaxrating,name="ajaxrating"),
    path('starrating/',views.starrating,name="starrating"),

    path('foodrating/<str:cid>',views.foodrating,name="foodrating"),
    path('ajaxfoodrating',views.ajaxfoodrating,name="ajaxfoodrating"),
    path('starfoodrating/',views.starfoodrating,name="starfoodrating"),

    path('boardingrating/<str:cid>',views.boardingrating,name="boardingrating"),
    path('ajaxboardingrating',views.ajaxboardingrating,name="ajaxboardingrating"),
    path('starboardingrating/',views.starboardingrating,name="starboardingrating"),
]