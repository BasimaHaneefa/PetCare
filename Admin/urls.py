from django.urls import path
from Admin import views

app_name="webadmin"

urlpatterns = [
    
    path('AdminRegistration/',views.adminreg,name="Admin Registration"),
    path('del_admin/<int:did>',views.del_admin,name="Del_admin"),
    path('edt_admin/<int:eid>',views.edt_admin,name="Edt_admin"),
    path('home/',views.HomePage,name="HomePage"),
    path('head/',views.head,name="head"),
    
    path('Logout/',views.logout,name="Logout"),
    
    path('ajax_category/',views.ajax_category,name="Ajax_Category"),
    
    path('District/',views.district,name="District"),
    path('del_district/<int:did>',views.del_district,name="Del_district"),
    path('edt_district/<int:eid>',views.edt_district,name="Edt_district"),

    path('Category/',views.category,name="Category"),
    path('del_category/<int:cid>',views.del_category,name="Del_category"),
    path('edt_category/<int:eid>',views.edt_category,name="Edt_category"),

    path('Place/',views.place,name="Place"),
    path('del_place/<int:did>',views.del_place,name="Del_place"),
    path('edt_place/<int:eid>',views.edt_place,name="Edt_place"),

    path('Sub Category/',views.subc,name="Sub Category"),
    path('del_sub/<int:did>',views.del_sub,name="Del_sub"),
    path('edt_sub/<int:eid>',views.edt_sub,name="Edt_sub"),

    path('ShopVerification/',views.shop,name="Shop Verification"),
    path('acceptshop/<int:aid>',views.acceptshop,name="Acc_shop"),
    path('rejectshop/<int:rid>',views.rejectshop,name="Rej_shop"),
    
    path('BreedType/',views.breed,name="Breed Type"),
    path('del_breed/<int:did>',views.del_breed,name="Del_breed"),
    
    path('HospitalVerification/',views.hospital,name="Hospital Verification"),
    path('accepthospital/<int:aid>',views.accepthospital,name="Acc_hospital"),
    path('rejecthospital/<int:rid>',views.rejecthospital,name="Rej_hospital"),
    
    path('PetBoardingVerification/',views.boarding,name="Boarding Verification"),
    path('acceptboarding/<int:aid>',views.acceptboarding,name="Acc_boarding"),
    path('rejectboarding/<int:rid>',views.rejectboarding,name="Rej_boarding"),
    
    path('AcceptedBoarding/',views.Acceptedboarding,name="Accepted Boarding"),
    path('RejectedBoarding/',views.Rejectedboarding,name="Rejected Boarding"),
    
    
    path('ViewComplaint/',views.viewc,name="View Complaint"),
    path('Replied/<int:replyid>',views.reply,name="Reply"),
    path('Viewfeedback/',views.viewf,name="View Feedback"),
    
    path('GroomingType/',views.grooming,name="Grooming"),
    path('del_grooming/<int:cid>',views.del_grooming,name="Del_grooming"),
    path('edt_grooming/<int:eid>',views.edt_grooming,name="Edt_grooming"),
    
    path('Report/',views.report,name="Report"),
]
