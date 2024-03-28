from django.shortcuts import render,redirect
from Guest.models import*
from Admin.models import*
from Shop.models import*
from User.models import tbl_feedback

#new lines Added
from django.core.mail import send_mail
from django.conf import settings
import random
#ended

# Create your views here.

def Maintemplate(request):
    feedback=tbl_feedback.objects.all()
    return render(request,"Guest/index.html",{'feedback':feedback})

def blog(request):
    foodcount=tbl_food.objects.all().count()
    hoscount=tbl_hospital.objects.all().count()
    productcount=tbl_product.objects.all().count()
    return render(request,"Guest/Blog.html",{'food':foodcount,'product':productcount,'hos':hoscount})

def ajax_place(request):
    disob=tbl_district.objects.get(id=request.GET.get('dist'))
    places=tbl_place.objects.filter(district=disob)
    return render(request,"Guest/AjaxPlace.html",{'plc':places})

def user(request):
    disObj=tbl_district.objects.all()
    if request.method=="POST":
        confirm=request.POST.get("confirmpass")
        password=request.POST.get("txtpass")
        plc=tbl_place.objects.get(id=request.POST.get('sel_place'))
        if confirm == password:
            tbl_user.objects.create(
                user_name=request.POST.get("txtname"),
                user_email=request.POST.get("txtemail"),
                user_cont=request.POST.get("txtno"),
                user_address=request.POST.get("txtadd"),
                user_password=request.POST.get("txtpass"),
                user_photo=request.FILES.get("filepic"),
                place=plc)
            msg="Registration Completed!!"
            return render(request,"Guest/User.html",{'msg':msg})
        else:
            msg="Password not matching!"
            return render(request,"Guest/User.html",{'msg':msg})
    else:
        return render(request,"Guest/User.html", {'disdata':disObj})
    
    
def login(request):
    if request.method=="POST":
        email=request.POST.get("txtemail")
        password=request.POST.get("txtpass")
        admincount=tbl_admin.objects.filter(admin_email=email,admin_password=password).count()
        usercount=tbl_user.objects.filter(user_email=email,user_password=password).count()
        hospitalcount=tbl_hospital.objects.filter(hospital_email=email,hospital_password=password,hospital_vstatus=1).count()
        shopcount=tbl_shop.objects.filter(shop_email=email,shop_password=password,shop_vstatus=1).count()
        boardcount=tbl_petboarding.objects.filter(boarding_email=email,boarding_password=password,boarding_status=1).count()
        if admincount>0:
            admin=tbl_admin.objects.get(admin_email=email,admin_password=password)
            request.session["adminid"]=admin.id
            request.session["aname"]=admin.admin_name
            return redirect("webadmin:HomePage")
        elif usercount>0:
            user=tbl_user.objects.get(user_email=email,user_password=password)  
            request.session["userid"]=user.id
            request.session["uname"]=user.user_name
            return redirect("webuser:UserHome")
        elif hospitalcount>0:
            hospital=tbl_hospital.objects.get(hospital_email=email,hospital_password=password)
            request.session["hospitalid"]=hospital.id
            request.session["hname"]=hospital.hospital_name
            return redirect("webhospital:HosHome")
        elif shopcount>0:
            shop=tbl_shop.objects.get(shop_email=email,shop_password=password)
            request.session["shopid"]=shop.id
            request.session["sname"]=shop.shop_name
            return redirect("webshop:ShopHome")
        elif boardcount>0:
            boarding=tbl_petboarding.objects.get(boarding_email=email,boarding_password=password)
            request.session["boardid"]=boarding.id
            request.session["boardname"]=boarding.boarding_name
            return redirect("webboarding:BoardHome")
        else:
            msg="Invalid Credentials!!"
            return render(request,"Guest/Login.html",{'msg':msg})
    else:
        return render(request,"Guest/Login.html") 
    
def shop(request):
    disObj=tbl_district.objects.all()
    if request.method=="POST":
        confirm=request.POST.get("confirmpass")
        password=request.POST.get("txtpass")
        plc=tbl_place.objects.get(id=request.POST.get('sel_place'))
        if confirm == password:
            tbl_shop.objects.create(
                shop_name=request.POST.get("txtname"),
                shop_email=request.POST.get("txtemail"),
                shop_contact=request.POST.get("txtcont"),
                shop_address=request.POST.get("txtadd"),
                shop_password=request.POST.get("txtpass"),
                shop_photo=request.FILES.get("filepic"),
                shop_proof=request.FILES.get("fileproof"),
                place=plc)
            msg="Registration Completed!!"
            return render(request,"Guest/Shopreg.html", {'disdata':disObj,'msg':msg})
        else:
            msg="Password not matching!"
            return render(request,"Guest/Shopreg.html", {'disdata':disObj,'msg':msg})
    else:
        return render(request,"Guest/Shopreg.html", {'disdata':disObj})
    
    
def hospital(request):
    disObj=tbl_district.objects.all()
    if request.method=="POST":
        confirm=request.POST.get("confirmpass")
        password=request.POST.get("txtpass")
        plc=tbl_place.objects.get(id=request.POST.get('sel_place'))
        if confirm == password:
            tbl_hospital.objects.create(
                hospital_name=request.POST.get("txtname"),
                hospital_email=request.POST.get("txtemail"),
                hospital_contact=request.POST.get("txtcont"),
                hospital_address=request.POST.get("txtadd"),
                hospital_password=request.POST.get("txtpass"),
                hospital_logo=request.FILES.get("filepic"),
                hospital_proof=request.FILES.get("fileproof"),
                place=plc)
            msg="Registration Completed!!"
            return render(request,"Guest/Hospitalreg.html", {'disdata':disObj,'msg':msg})
        else:
            msg="Password not matching!"
            return render(request,"Guest/Hospitalreg.html", {'disdata':disObj,'msg':msg})
    else:
        return render(request,"Guest/Hospitalreg.html", {'disdata':disObj})
    
def petboarding(request):
    disObj=tbl_district.objects.all()
    if request.method=="POST":
        confirm=request.POST.get("confirmpass")
        password=request.POST.get("txtpass")
        plc=tbl_place.objects.get(id=request.POST.get('sel_place'))
        if confirm == password:
            tbl_petboarding.objects.create(
                boarding_name=request.POST.get("txtname"),
                boarding_email=request.POST.get("txtemail"),
                boarding_contact=request.POST.get("txtcont"),
                boarding_address=request.POST.get("txtadd"),
                boarding_password=request.POST.get("txtpass"),
                boarding_logo=request.FILES.get("filepic"),
                boarding_proof=request.FILES.get("fileproof"),
                place=plc)
            msg="Registration Completed!!"
            return render(request,"Guest/PetBoardingReg.html", {'disdata':disObj,'msg':msg})
        else:
            msg="Password not matching!"
            return render(request,"Guest/PetBoardingReg.html", {'disdata':disObj,'msg':msg})
    else:
        return render(request,"Guest/PetBoardingReg.html", {'disdata':disObj})
    
# New Functions
def ForgetPassword(request):
    
    if request.method=="POST":
        otp=random.randint(10000, 999999)
        request.session["otp"]=otp
        request.session["femail"]=request.POST.get('txtemail')
        send_mail(
            'Respected Sir/Madam ',#subject
            "\rYour OTP for Reset Password is"+str(otp),#body
            settings.EMAIL_HOST_USER,
            [request.POST.get('txtemail')],
        )
        return redirect("webguest:verification")
    else:
        return render(request,"Guest/ForgetPassword.html")

def OtpVerification(request):
    if request.method=="POST":
        otp=int(request.session["otp"])
        if int(request.POST.get('txtotp'))==otp:
            return redirect("webguest:create")
        else:
            msg="Invalid OTP!!"
            return render(request,"Guest/OTPVerification.html",{'msg':msg})
    return render(request,"Guest/OTPVerification.html")

def CreateNewPass(request):
    if request.method=="POST":
        if request.POST.get('txtpassword2')==request.POST.get('txtpassword3'):
            usercount=tbl_user.objects.filter(user_email=request.session["femail"]).count()
            shopcount=tbl_shop.objects.filter(shop_email=request.session["femail"]).count()
            boardcount=tbl_petboarding.objects.filter(boarding_email=request.session["femail"]).count()
            hospitalcount=tbl_hospital.objects.filter(hospital_email=request.session["femail"]).count()
            if usercount>0:
                user=tbl_user.objects.get(user_email=request.session["femail"])
                user.user_password=request.POST.get('txtpassword2')
                user.save()
                msg="Password Changed Successfully.."
                return render(request,"Guest/Login.html",{'msg':msg})

            elif shopcount>0:
                doc=tbl_shop.objects.get(shop_email=request.session["femail"])
                doc.shop_password=request.POST.get('txtpassword2')
                doc.save()
                msg="Password Changed Successfully.."
                return render(request,"Guest/Login.html",{'msg':msg})

            elif boardcount>0:
                board=tbl_petboarding.objects.get(boarding_email=request.session["femail"])
                board.boarding_password=request.POST.get('txtpassword2')
                board.save()
                msg="Password Changed Successfully.."
                return render(request,"Guest/Login.html",{'msg':msg})
            
            elif hospitalcount>0:
                hos=tbl_hospital.objects.get(hospital_email=request.session["femail"])
                hos.hospital_password=request.POST.get('txtpassword2')
                hos.save()
                msg="Password Changed Successfully.."
                return render(request,"Guest/Login.html",{'msg':msg})
            else:
                msg="Something happened,Please try later..."
                return render(request,"Guest/Login.html",{'msg':msg})
        else:
            msg="Failed to Change Password.Password miss match!"
            return render(request,"Guest/CreateNewPassword.html",{'msg':msg})
    else:       
        return render(request,"Guest/CreateNewPassword.html")


#New Functions End