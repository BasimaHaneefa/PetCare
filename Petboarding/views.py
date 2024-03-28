from django.shortcuts import render,redirect
from Petboarding.models import *
from Guest.models import*
from Admin.models import *
from User.models import *

# Create your views here.

def BoardHome(request):
    if 'boardid' in request.session:
        boarding_name=request.session["boardname"]
        boardingObj=tbl_petboarding.objects.get(id=request.session["boardid"])
        staff=tbl_staff.objects.filter(boarding=boardingObj)
        return render(request,"Petboarding/BoardHome.html",{'board':boarding_name, 'boards':boardingObj, 'staff':staff})
    else:
        return redirect("webguest:Login")
    
def logout(request):
    if 'boardid' in request.session:
        del request.session["boardid"]
        return redirect("webguest:Main Index")
    else:
        return redirect("webguest:Login")
       
def myprofile(request):
    boardingObj=tbl_petboarding.objects.get(id=request.session["boardid"])
    return render(request,"Petboarding/MyProfile.html",{'datas':boardingObj})
    
def editprofile(request):
    boardingObj=tbl_petboarding.objects.get(id=request.session["boardid"])
    if request.method=="POST":
        boardingObj.boarding_name=request.POST.get("txtname")
        boardingObj.boarding_address=request.POST.get("txtadd")
        boardingObj.boarding_contact=request.POST.get("txtno")
        boardingObj.boarding_email=request.POST.get("txtemail")
        boardingObj.save()
        return redirect('webboarding:Profile')
    else:
        return render(request,"Petboarding/EditMyProfile.html",{'data':boardingObj })
    
def password(request):
    if request.method=="POST":
        s=tbl_petboarding.objects.get(id=request.session["boardid"],boarding_password=request.POST.get("txt"))
        cpass=request.POST.get("txtconfirm")
        new=request.POST.get("txtnew")
        if cpass==new:
            s.boarding_password=request.POST.get("txtconfirm")
            s.save()
            msg="Password Updated!!"
            return redirect('webboarding:Profile')
        else:
            msg="Password Mismatch!!"
            return render(request,"Petboarding/ChangePass.html",{'msg':msg})
    else:
        return render(request,"Petboarding/ChangePass.html") 

def gdatails(request):
    boardObj=tbl_petboarding.objects.get(id=request.session["boardid"])
    gObj=tbl_groomingtype.objects.all()
    dObj=tbl_gdetails.objects.filter(boarding=boardObj)
    if request.method=="POST":
        gid=tbl_groomingtype.objects.get(id=request.POST.get("sel_groom"))
        bid=tbl_petboarding.objects.get(id=request.session["boardid"])
        pet_details=request.POST.getlist("txtcheck[]")
        tbl_gdetails.objects.create(gd_details=request.POST.get("txtdetails"),
                                    gd_photo=request.FILES.get("filepic"),
                                    gd_pets=', '.join(pet_details),
                                    grooming=gid,
                                    boarding=bid)
        return render(request,"Petboarding/GroomingDetails.html",{'datag':gObj, 'datas':dObj,'data':boardObj})
    else:
        return render(request,"Petboarding/GroomingDetails.html",{'datag':gObj, 'datas':dObj,'data':boardObj})

def del_gdetails(request,did):
    tbl_gdetails.objects.get(id=did).delete()
    return redirect('webboarding:Grooming Details')

def staff(request):
    bObj=tbl_petboarding.objects.get(id=request.session["boardid"])
    gObj=tbl_groomingtype.objects.all()
    sObj=tbl_staff.objects.filter(boarding=bObj)
    if request.method=="POST":
        groom=tbl_groomingtype.objects.get(id=request.POST.get('sel_groom'))
        bid=tbl_petboarding.objects.get(id=request.session["boardid"])
        tbl_staff.objects.create(
            staff_name=request.POST.get("txtname"),
            staff_email=request.POST.get("txtemail"),
            staff_contact=request.POST.get("txtcont"),
            staff_gender=request.POST.get("txtgender"),
            staff_address=request.POST.get("txtadd"),
            staff_photo=request.FILES.get("filepic"),
            staff_proof=request.FILES.get("fileproof"),
            grooming=groom,
            boarding=bid)
        msg="Registration Completed!!"
        return render(request,"Petboarding/StaffRegistration.html", {'datag':gObj,'datas':sObj,'msg':msg})
    else:
        return render(request,"Petboarding/StaffRegistration.html", {'datag':gObj,'datas':sObj})

def del_staff(request,did):
    tbl_staff.objects.get(id=did).delete()
    return redirect('webboarding:Staff Registration')

def gallery(request,gid):
    gdObj=tbl_gdetails.objects.get(id=gid)
    galleryObj=tbl_gallery.objects.filter(gd=gdObj)
    if request.method=="POST":
        gdid=tbl_gdetails.objects.get(id=gid)
        tbl_gallery.objects.create(gallery_caption=request.POST.get("txtcaption"),
                                    gallery_photo=request.FILES.get("filepic"),
                                    gd=gdid)
        return render(request,"Petboarding/AddGallery.html",{'data':galleryObj})
    else:
        return render(request,"Petboarding/AddGallery.html",{'data':galleryObj})
    
def del_gallery(request,did):
    tbl_gallery.objects.get(id=did).delete()
    return redirect('webboarding:Grooming Details')

def viewuserbapp(request):
    bObj=tbl_petboarding.objects.get(id=request.session["boardid"])
    bappObj=tbl_boardingappointment.objects.filter(boarding=bObj, booking_status=0)
    if request.method=="POST":
        return render(request,"Petboarding/ViewUserAppointment.html",{'data':bappObj})
    else:
        return render(request,"Petboarding/ViewUserAppointment.html",{'data':bappObj})
    
def acceptuser(request, aid):
    bappdata=tbl_boardingappointment.objects.get(id=aid)
    bappdata.booking_status=1
    bappdata.save()
    return redirect('webboarding:View User Appointment')
   
def rejectuser(request, rid):
    bappdata=tbl_boardingappointment.objects.get(id=rid)
    bappdata.booking_status=2
    bappdata.save()
    return redirect('webboarding:View User Appointment')

def viewusergapp(request):
    bObj=tbl_petboarding.objects.get(id=request.session["boardid"])
    gappObj=tbl_groomingappointment.objects.filter(boarding=bObj, gappointment_status=0)
    if request.method=="POST":
        return render(request,"Petboarding/ViewUserGAppointment.html",{'data':gappObj})
    else:
        return render(request,"Petboarding/ViewUserGAppointment.html",{'data':gappObj})
    
def acceptgappointment(request, aid):
    gappdata=tbl_groomingappointment.objects.get(id=aid)
    gappdata.gappointment_status=1
    gappdata.save()
    return redirect('webboarding:View User Grooming Appointment')
   
def rejectgappointment(request, rid):
    gappdata=tbl_groomingappointment.objects.get(id=rid)
    gappdata.gappointment_status=2
    gappdata.save()
    return redirect('webboarding:View User Grooming Appointment')