from django.urls import path
from Guest import views

app_name="webguest"

urlpatterns = [
    path('',views.Maintemplate,name="Main Index"),
    
    path('Blog/',views.blog,name="Blog"),
    
    path('ajax_place/',views.ajax_place,name="Ajax_Place"),
    
    path('Shopreg/',views.shop,name="Shop Registration"),
    
    path('Login/',views.login,name="Login"),
    
    path('User/',views.user,name="User Registration"),
    
    path('Hospitalreg/',views.hospital,name="Hospital Registration"),
    
    path('PetBoardingReg/',views.petboarding,name="Pet Boarding Registration"),
    
    path('fpass/', views.ForgetPassword,name="forpass"),
    path('otpver/', views.OtpVerification,name="verification"),
    path('create/', views.CreateNewPass,name="create"),
]