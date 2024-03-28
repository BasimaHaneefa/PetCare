from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
from django.db.models import Sum


# Create your views here.
def HomePage(request):
    if 'adminid' in request.session:
        admin_name=request.session["aname"]
        growth=tbl_booking.objects.all()
        totalgrowth = growth.aggregate(totalgrowth=Sum('totalamount'))['totalgrowth']
        shopcount=tbl_shop.objects.filter(shop_vstatus=1).count()
        hospitalcount=tbl_hospital.objects.filter(hospital_vstatus=1).count()
        usercount=tbl_user.objects.all().count()
        booking=tbl_booking.objects.filter(booking_status=1)
        complaint=tbl_complaint.objects.all()
        feedback=tbl_feedback.objects.all()
        return render(request,"Admin/HomePage.html",{'admin':admin_name,'totalgrowth':totalgrowth,'shop':shopcount,'hospital':hospitalcount,'user':usercount,
                                                     'booking':booking,'complaint':complaint,'feedback':feedback})
    else:
        return redirect("webguest:Login")

def head(request):
    if 'adminid' in request.session:
        admin_name=request.session["aname"]
        
        return render(request,"Admin/HeadFooter.html",{'admin':admin_name,})
    else:
        return redirect("webguest:Login")
    
def logout(request):
    if 'adminid' in request.session:
        del request.session["adminid"]
        return redirect("webguest:Main Index")
    else:
        return redirect("webguest:Login")

def adminreg(request):
    adminObj=tbl_admin.objects.all()
    if request.method=="POST":
        tbl_admin.objects.create(admin_name=request.POST.get("txtname"),admin_email=request.POST.get("txtemail"),admin_cont=request.POST.get("txtcon"),admin_password=request.POST.get("txtpass"))
        return render(request,"Admin/AdminRegistration.html",{'datas':adminObj})
    else:
        return render(request,"Admin/AdminRegistration.html",{'datas':adminObj})

def del_admin(request,did):
    tbl_admin.objects.get(id=did).delete()
    return redirect('webadmin:Admin Registration')

def edt_admin(request,eid):
    admindata=tbl_admin.objects.get(id=eid)
    adminObj=tbl_admin.objects.all()
    if request.method=="POST":
        admindata.admin_name=request.POST.get("txtname")
        admindata.admin_email=request.POST.get("txtemail")
        admindata.admin_cont=request.POST.get("txtcon")
        admindata.admin_password=request.POST.get("txtpass")
        admindata.save()
        return redirect('webadmin:Admin Registration')
    else:
        return render(request,"Admin/AdminRegistration.html",{'addata':admindata, 'datas':adminObj})

def district(request):
    if 'adminid' in request.session:
        disObj=tbl_district.objects.all()
        if request.method=="POST":
            tbl_district.objects.create(district_name=request.POST.get("txt_district"))
            return render(request,"Admin/District.html",{'data':disObj})
        else:
            return render(request,"Admin/District.html",{'data':disObj})
    else:
        return redirect("webguest:Login")    


def del_district(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect('webadmin:District')

def edt_district(request,eid):
    disdata=tbl_district.objects.get(id=eid)
    disObj=tbl_district.objects.all()
    if request.method=="POST":
        disdata.district_name=request.POST.get("txt_district")
        disdata.save()
        return redirect('webadmin:District')
    else:
        return render(request,"Admin/District.html",{'ddata':disdata,'data':disObj})

def place(request):
    disObj=tbl_district.objects.all()
    placeObj=tbl_place.objects.all()
    if request.method=="POST":
        disid=tbl_district.objects.get(id=request.POST.get("sel_district"))
        tbl_place.objects.create(place_name=request.POST.get("txt_place"),place_pin=request.POST.get("txt_pin"),district=disid)
        return render(request,"Admin/Place.html",{'disdata':disObj, 'dplace':placeObj})
    else:
        return render(request,"Admin/Place.html",{'disdata':disObj, 'dplace':placeObj})

def del_place(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect('webadmin:Place')

def edt_place(request,eid):
    pdata=tbl_place.objects.get(id=eid)
    disObj=tbl_district.objects.all()
    if request.method=="POST":
        pdata.place_name=request.POST.get("txt_place")
        pdata.place_pin=request.POST.get("txt_pin")
        pdata.district_id=request.POST.get("sel_district")
        pdata.save()
        return redirect('webadmin:Place')
    else:
        return render(request,"Admin/Place.html",{'pldata':pdata, 'disdata':disObj })


def category(request):
    catObj=tbl_category.objects.all()
    if request.method=="POST":
        tbl_category.objects.create(category_name=request.POST.get("txt_category"))
        return render(request,"Admin/Category.html",{'data':catObj})
    else:
        return render(request,"Admin/Category.html",{'data':catObj})
  
def del_category(request,cid):
    tbl_category.objects.get(id=cid).delete()
    return redirect('webadmin:Category')

def edt_category(request,eid):
    catdata=tbl_category.objects.get(id=eid)
    disObj=tbl_category.objects.all()
    if request.method=="POST":
        catdata.category_name=request.POST.get("txt_category")
        catdata.save()
        return redirect('webadmin:Category')
    else:
        return render(request,"Admin/Category.html",{'cdata':catdata, 'data':disObj})

def subc(request):
    catObj=tbl_category.objects.all()
    subObj=tbl_subcategory.objects.all()
    if request.method=="POST":
        catid=tbl_category.objects.get(id=request.POST.get("sel_cat"))
        tbl_subcategory.objects.create(sub_name=request.POST.get("txt_sub"),category=catid)
        return render(request,"Admin/SubCategory.html",{'subdata':catObj, 'datas':subObj})
    else:
        return render(request,"Admin/SubCategory.html",{'subdata':catObj, 'datas':subObj})

def del_sub(request,did):
    tbl_subcategory.objects.get(id=did).delete()
    return redirect('webadmin:Sub Category')

def edt_sub(request,eid):
    subdata=tbl_subcategory.objects.get(id=eid)
    catObj=tbl_category.objects.all()
    if request.method=="POST":
        subdata.sub_name=request.POST.get("txt_sub")
        subdata.category_id=request.POST.get("sel_cat")
        subdata.save()
        return redirect('webadmin:Sub Category')
    else:
        return render(request,"Admin/SubCategory.html",{'sdata':subdata, 'subdata':catObj })

def grooming(request):
    gObj=tbl_groomingtype.objects.all()
    if request.method=="POST":
        tbl_groomingtype.objects.create(grooming_type=request.POST.get("txt_groom"))
        return render(request,"Admin/GroomingType.html",{'data':gObj})
    else:
        return render(request,"Admin/GroomingType.html",{'data':gObj})
  
def del_grooming(request,cid):
    tbl_groomingtype.objects.get(id=cid).delete()
    return redirect('webadmin:Grooming')

def edt_grooming(request,eid):
    gObj=tbl_groomingtype.objects.get(id=eid)
    groomObj=tbl_groomingtype.objects.all()
    if request.method=="POST":
        gObj.grooming_type=request.POST.get("txt_groom")
        gObj.save()
        return redirect('webadmin:Grooming')
    else:
        return render(request,"Admin/GroomingType.html",{'gdata':gObj, 'data':groomObj})
    
def shop(request):
    shopObj=tbl_shop.objects.filter(shop_vstatus=0)
    if request.method=="POST":
        return render(request,"Admin/ShopVerification.html",{'datas':shopObj})
    else:
        return render(request,"Admin/ShopVerification.html",{'datas':shopObj})
    
def acceptshop(request, aid):
    shopdata=tbl_shop.objects.get(id=aid)
    shopdata.shop_vstatus=1
    shopdata.save()
    return redirect('webadmin:Shop Verification')
    
def rejectshop(request, rid):
    shopdata=tbl_shop.objects.get(id=rid)
    shopdata.shop_vstatus=2
    shopdata.save()
    return redirect('webadmin:Shop Verification')

def ajax_category(request):
    catob=tbl_category.objects.get(id=request.GET.get('cat'))
    sub=tbl_subcategory.objects.filter(category=catob)
    return render(request,"Admin/AjaxCategory.html",{'su':sub})

def breed(request):
    breedObj=tbl_breedtype.objects.all()
    catObj=tbl_category.objects.all()
    if request.method=="POST":
        sub=tbl_subcategory.objects.get(id=request.POST.get('sel_sub'))
        tbl_breedtype.objects.create(breed_name=request.POST.get("txtname"),
                                     subcategory=sub)
        return render(request,"Admin/BreedType.html",{'datas':catObj, 'data':breedObj})
    else:
        return render(request,"Admin/BreedType.html",{'datas':catObj, 'data':breedObj})
    
def del_breed(request,did):
    tbl_breedtype.objects.get(id=did).delete()
    return redirect('webadmin:Breed Type')

def edt_breed(request,eid):
    breeddata=tbl_breedtype.objects.get(id=eid)
    breedObj=tbl_breedtype.objects.all()
    catObj=tbl_category.objects.all()
    subObj=tbl_subcategory.objects.all()
    if request.method=="POST":
        breeddata.breed_name=request.POST.get("txtname")
        breeddata.category_id=request.POST.get("sel_cat")
        breeddata.save()
        return redirect('webadmin:Breed Type')
    else:
        return render(request,"Admin/BreedType.html",{'bdata':breeddata, 'data':breedObj})
    
def hospital(request):
    hosObj=tbl_hospital.objects.filter(hospital_vstatus=0)
    if request.method=="POST":
        return render(request,"Admin/HospitalVerification.html",{'datas':hosObj})
    else:
        return render(request,"Admin/HospitalVerification.html",{'datas':hosObj})
    
def accepthospital(request, aid):
    hospitaldata=tbl_hospital.objects.get(id=aid)
    hospitaldata.hospital_vstatus=1
    hospitaldata.save()
    return redirect('webadmin:Hospital Verification')
    
def rejecthospital(request, rid):
    hospitaldata=tbl_hospital.objects.get(id=rid)
    hospitaldata.hospital_vstatus=2
    hospitaldata.save()
    return redirect('webadmin:Hospital Verification')

def viewc(request):
    comObj=tbl_complaint.objects.filter(complaint_status=1)
    if request.method=="POST":
        return render(request,"Admin/ViewComplaint.html",{'datas':comObj})
    else:
        return render(request,"Admin/ViewComplaint.html",{'datas':comObj})
    
def reply(request,replyid):
    comObj=tbl_complaint.objects.filter(complaint_status=0)
    replydata=tbl_complaint.objects.get(id=replyid)
    if request.method=="POST":
        replydata.complaint_reply=request.POST.get("txtreply")
        replydata.complaint_status=1
        replydata.save()
        return redirect('webadmin:View Complaint')
    else:
        return render(request,"Admin/Reply.html",{'datas':comObj})
    
def viewf(request):
    feedObj=tbl_feedback.objects.all()
    if request.method=="POST":
        return render(request,"Admin/ViewFeedback.html",{'datas':feedObj})
    else:
        return render(request,"Admin/ViewFeedback.html",{'datas':feedObj})
    
def boarding(request):
    boardingObj=tbl_petboarding.objects.filter(boarding_status=0)
    if request.method=="POST":
        return render(request,"Admin/BoardingVerification.html",{'board':boardingObj})
    else:
        return render(request,"Admin/BoardingVerification.html",{'board':boardingObj})
    
def acceptboarding(request, aid):
    boardingdata=tbl_petboarding.objects.get(id=aid)
    boardingdata.boarding_status=1
    boardingdata.save()
    return redirect('webadmin:Boarding Verification')
   
def rejectboarding(request, rid):
    boardingdata=tbl_petboarding.objects.get(id=rid)
    boardingdata.boarding_status=2
    boardingdata.save()
    return redirect('webadmin:Boarding Verification')

def Acceptedboarding(request):
    boarding=tbl_petboarding.objects.filter(boarding_status=1)
    if request.method=="POST":
        return render(request,"Admin/AccPetBoarding.html",{'board':boarding})
    else:
        return render(request,"Admin/AccPetBoarding.html",{'board':boarding})
    
def Rejectedboarding(request):
    boardingObj=tbl_petboarding.objects.filter(boarding_status=2)
    
    if request.method=="POST":
        return render(request,"Admin/RejPetBoarding.html",{'board':boardingObj})
    else:
        return render(request,"Admin/RejPetBoarding.html",{'board':boardingObj})
    
def report(request):
    if 'adminid' in request.session:
        booking=tbl_booking.objects.filter(booking_status=1)
        if request.method=="POST":
            bdata=tbl_booking.objects.filter(booking_status=1,booking_date__gt=request.POST.get('txtdate'),booking_date__lt=request.POST.get('txt_date'))
            return render(request, "Admin/Report.html",{'booking':bdata})
        else:
            return render(request, "Admin/Report.html",{'booking':booking})
    else:
        return redirect("webguest:Login")