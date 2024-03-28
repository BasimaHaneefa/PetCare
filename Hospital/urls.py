from django.urls import path
from Hospital import views

app_name="webhospital"

urlpatterns = [
    path('Home/',views.HomePage,name="HosHome"),
    
    path('Logout/',views.logout,name="Logout"),
    
    path('myprofile/',views.myprofile,name="Profile"),
    
    path('Editprofile/',views.editprofile,name="Edit Profile"),
    
    path('changepass/',views.password,name="Change Password"),
    
    path('adddoctors/',views.doctor,name="Add Doctor"),
    path('deldoctor/<int:did>',views.deldoctor,name="Deldoctor"),
    
    path('ViewUserAppointment/',views.viewappointment,name="View User Appointment"),
    path('accept/<int:aid>',views.acceptappointment,name="Accept"),
    path('reject/<int:rid>',views.rejectappointment,name="Reject"),
    path('Vaccination/<int:vaccid>',views.Vaccination,name="Vaccination"),
    
    path('AcceptedAppointment/',views.Acceptedappointment,name="Accepted Appointment"),
    path('RejectedAppointment/',views.Rejectedappointment,name="Rejected Appointment"),
    
    path('ViewDoctor/',views.viewdoctor,name="View Doctor List"),
    path('viewuserchat<int:doctor_id>/',views.view_user_chat,name="View user"),
    
    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),
    
]