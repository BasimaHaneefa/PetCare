from django.urls import path
from Petboarding import views
from Guest.models import *

app_name="webboarding"

urlpatterns = [
    path('HomePage/',views.BoardHome,name="BoardHome"),
    
    path('Logout/',views.logout,name="Logout"),
    
    path('myprofile/',views.myprofile,name="Profile"),   
    path('Editprofile/',views.editprofile,name="Edit Profile"),
    path('changepassword/',views.password,name="Change Password"),
    
    path('GroomingDetails/',views.gdatails,name="Grooming Details"),
    path('Delgd/<int:did>',views.del_gdetails,name="Delgd"),
    
    path('StaffRegistration/',views.staff,name="Staff Registration"),
    path('Delstaff/<int:did>',views.del_staff,name="Delstaff"),
    
    path('AddGallery/<int:gid>',views.gallery,name="Add Gallery"),
    path('Delgallery/<int:did>',views.del_gallery,name="Delgallery"),
    
    path('ViewUserAppointment/',views.viewuserbapp,name="View User Appointment"),
    path('acceptappointment/<int:aid>',views.acceptuser,name="Acc_appointment"),
    path('rejectappointmentg/<int:rid>',views.rejectuser,name="Rej_appointment"),
    
    path('ViewUserGAppointment/',views.viewusergapp,name="View User Grooming Appointment"),
    path('acceptgappointment/<int:aid>',views.acceptgappointment,name="Acc_gappointment"),
    path('rejectgappointmentg/<int:rid>',views.rejectgappointment,name="Rej_gappointment"),
]