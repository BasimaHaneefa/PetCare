import datetime
from django.http import JsonResponse
from django.shortcuts import render, redirect
from User.models import *
from Guest.models import *
from Admin.models import *
from Hospital.models import *
from Shop.models import *
from Petboarding.models import *
from django.db.models import Q
from datetime import datetime, date
from django.utils import timezone

# Create your views here.

def HomePage(request):
    if 'userid' in request.session:
        user_name = request.session["uname"]
        docObj=tbl_doctor.objects.all()
        petObj=tbl_pet.objects.all()
        shopObj=tbl_shop.objects.filter(shop_vstatus=1)
        pets = tbl_petdetails.objects.filter(user=request.session["userid"])

        pet_data = []

        for pet in pets:
            petname = pet.breedtype_name
            vaccinedate = pet.pet_vaccinedate
            today = date.today()
            if vaccinedate !="":
                numberofdays = (today - vaccinedate).days

                if numberofdays >= 30:
                    msg = f"Take Appointment for Vaccination for {petname}"
                else:
                    msg = "Welcome"

                pet_data.append({'petname': petname, 'vaccinedate': vaccinedate, 'numberofdays': numberofdays, 'msg': msg})
                print(pet_data)

                return render(request, "User/UserHome.html", {'user': user_name, 'pet_data': pet_data, 'Doc': docObj, 'Pet': petObj, 'Shop':shopObj})
            else:
                return render(request, "User/UserHome.html")
    else:
        return redirect("webguest:Login")
    
def logout(request):
    if 'userid' in request.session:
        del request.session["userid"]
        return redirect("webguest:Main Index")
    else:
        return redirect("webguest:Login")

def myprofile(request):
    if 'userid' in request.session:
        userObj=tbl_user.objects.get(id=request.session["userid"])
        return render(request,"User/MyProfile.html",{'datas':userObj})
    else:
        return redirect("webguest:Login")
    
def editprofile(request):
    if 'userid' in request.session:
        userObj=tbl_user.objects.get(id=request.session["userid"])
        if request.method=="POST":
            userObj.user_name=request.POST.get("txtname")
            userObj.user_address=request.POST.get("txtadd")
            userObj.user_cont=request.POST.get("txtno")
            userObj.user_email=request.POST.get("txtemail")
            userObj.save()
            return redirect('webuser:My Profile')
        else:
            return render(request,"User/EditProfile.html",{'userdata':userObj })
    else:
        return redirect("webguest:Login")
    
def password(request):
    if 'userid' in request.session:
        if request.method=="POST":
            user=tbl_user.objects.get(id=request.session["userid"],user_password=request.POST.get("txt"))
            cpass=request.POST.get("txtconfirm")
            new=request.POST.get("txtnew")
            if cpass==new:
                user.user_password=request.POST.get("txtconfirm")
                user.save()
                msg="Password Changed.."
                return render(request,"User/ChangePassword.html",{'msg':msg})
            else:
                msg="Password Mismatch!!"
                return render(request,"User/ChangePassword.html",{'msg':msg})
        else:
                return render(request,"User/ChangePassword.html")
    else:
        return redirect("webguest:Login")
        
def petdetails(request):
    if 'userid' in request.session:
        petObj=tbl_petdetails.objects.filter(user=request.session["userid"])
        if request.method=="POST":
            us=tbl_user.objects.get(id=request.session["userid"])
            vdate=request.POST.get("txtv")
            if vdate != "":
                tbl_petdetails.objects.create(
                pet_dob=request.POST.get("txtdate"),
                breedtype_name=request.POST.get("txt_name"),
                pet_weight=request.POST.get("txtw"),
                pet_vaccinedate=request.POST.get("txtv"),
                pet_details=request.POST.get("txtdetails"),
                pet_vaccinename=request.POST.get("txtvacc"),
                pet_gender=request.POST.get("txtgender"),
                pet_photo=request.FILES.get("filepic"),
                user=us)
                return render(request,"User/Petdetails.html", {'data':petObj})
            else:
                tbl_petdetails.objects.create(
                pet_dob=request.POST.get("txtdate"),
                breedtype_name=request.POST.get("txt_name"),
                pet_weight=request.POST.get("txtw"),
                # pet_vaccinedate=request.POST.get("txtv"),
                pet_details=request.POST.get("txtdetails"),
                # pet_vaccinename=request.POST.get("txtvacc"),
                pet_gender=request.POST.get("txtgender"),
                pet_photo=request.FILES.get("filepic"),
                user=us)
                return render(request,"User/Petdetails.html", {'data':petObj})
        else:
            return render(request,"User/Petdetails.html", {'data':petObj})
    else:
        return redirect("webguest:Login")
    
def delpet(request,did):
    tbl_petdetails.objects.get(id=did).delete()
    return redirect('webuser:Pet Details')

def edtpet(request,eid):
    pdata=tbl_petdetails.objects.get(id=eid)
    petObj=tbl_petdetails.objects.all()
    if request.method=="POST":
        pdata.pet_dob=request.POST.get("txtdate")
        pdata.breedtype_name=request.POST.get("txt_name")
        pdata.pet_weight=request.POST.get("txtw")
        pdata.pet_vaccinedate=request.POST.get("txtv")
        pdata.pet_details=request.POST.get("txtdetails")
        pdata.pet_vaccinename=request.POST.get("txtvacc")
        pdata.pet_gender=request.POST.get("txtgender")
        pdata.pet_photo=request.FILES.get("filepic")
        pdata.save()
        return redirect('webuser:Pet Details')
    else:
        return render(request,"User/Petdetails.html",{'petdata':pdata, 'data':petObj })
    
def complaint(request):
    if 'userid' in request.session:
        comObj=tbl_complaint.objects.filter(user=request.session["userid"])
        if request.method=="POST":
            us=tbl_user.objects.get(id=request.session["userid"])
            tbl_complaint.objects.create(
                complaint_title=request.POST.get("txt"),
                complaint_content=request.POST.get("txtname"),
                user=us)
            return render(request,"User/Complaint.html", {'data':comObj})
        else:
            return render(request,"User/Complaint.html", {'data':comObj})
    else:
        return redirect("webguest:Login")
    
def delc(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect('webuser:Complaint')

def edtc(request,eid):
    cdata=tbl_complaint.objects.get(id=eid)
    comObj=tbl_complaint.objects.all()
    if request.method=="POST":
        cdata.complaint_title=request.POST.get("txt")
        cdata.complaint_content=request.POST.get("txtname")
        cdata.save()
        return redirect('webuser:Complaint')
    else:
        return render(request,"User/Complaint.html",{'datac':cdata, 'data':comObj })
    
def feedback(request):
    if 'userid' in request.session:
        feedObj=tbl_feedback.objects.filter(user=request.session["userid"])
        if request.method=="POST":
            us=tbl_user.objects.get(id=request.session["userid"])
            tbl_feedback.objects.create(
                feedback_content=request.POST.get("txt"),
                user=us)
            return render(request,"User/Feedback.html", {'data':feedObj})
        else:
            return render(request,"User/Feedback.html", {'data':feedObj})
    else:
        return redirect("webguest:Login")
    
def delf(request,did):
    tbl_feedback.objects.get(id=did).delete()
    return redirect('webuser:Feedback')

def edtf(request,eid):
    fdata=tbl_feedback.objects.get(id=eid)
    feedObj=tbl_feedback.objects.filter(user=request.session["userid"])
    if request.method=="POST":
        fdata.feedback_content=request.POST.get("txt")
        fdata.save()
        return redirect('webuser:Feedback')
    else:
        return render(request,"User/Feedback.html",{'dataf':fdata, 'data':feedObj })
    

def searchHos(request):
    if 'userid' in request.session:
        disObj=tbl_district.objects.all()
        HosObj=tbl_hospital.objects.filter(hospital_vstatus=1)
        return render(request,"User/SearchHospital.html",{'datas':HosObj, 'disdata':disObj})  
    else:
        return redirect("webguest:Login")

def ajax_search(request):
    placedata=tbl_place.objects.get(id=request.GET.get('search'))
    HosObj=tbl_hospital.objects.filter(place=placedata,hospital_vstatus=1)
    return render(request,"User/AjaxSearch.html",{'hos':HosObj})

def viewdoctor(request,vid):
    if 'userid' in request.session:
        HosObj=tbl_hospital.objects.get(id=vid)
        docdata=tbl_doctor.objects.filter(hospital=HosObj)
        return render(request,"User/ViewDoctor.html",{'datas':docdata, 'data':HosObj}) 
    else:
        return redirect("webguest:Login")
 

def searchProduct(request):
    if 'userid' in request.session:
        ar=[1,2,3,4,5]
        catObj=tbl_category.objects.all()
        shopdata=tbl_shop.objects.get(shop_vstatus=1)
        ProObj=tbl_product.objects.filter(shop=shopdata)
        avg_list = []  # Create a list to store average ratings for each car
        reviewcount = 0
        for c in ProObj:
            reviewcount = tbl_review.objects.filter(product=c.id).count()
        # print(reviewcount)
            res = 0
            avg = 0
            review = tbl_review.objects.filter(product=c.id)
            for rev in review:
                res = res + rev.user_rating
                # print(res)
                avg = res//reviewcount
                # print(avg)
            avg_list.append(avg)
        print(avg_list)
        cdata = zip(ProObj,avg_list)
        return render(request,"User/SearchProduct.html",{'data':cdata, 'datas':catObj, "avg": avg_list,"ar":ar})  
    else:
        return redirect("webguest:Login")

def ajax_product(request):
    subdata=tbl_subcategory.objects.get(id=request.GET.get('search'))
    shopdata=tbl_shop.objects.get(shop_vstatus=1)
    ProObj=tbl_product.objects.filter(subc=subdata,shop=shopdata)
    return render(request,"User/AjaxProduct.html",{'pro':ProObj})

def buyproduct(request,pid):
    if 'userid' in request.session:
        prodata=tbl_product.objects.get(id=pid)
        custdata=tbl_user.objects.get(id=request.session["userid"])
        bookingcount=tbl_booking.objects.filter(user=custdata,booking_status=0).count()
        if bookingcount>0:
            bookingdata=tbl_booking.objects.get(user=custdata,booking_status=0)
            cartcount=tbl_cart.objects.filter(booking=bookingdata,product=prodata).count()
            if cartcount>0:
                msg="Already added"
                return render(request,"User/SearchProduct.html",{'msg':msg})
            else:
                tbl_cart.objects.create(booking=bookingdata,product=prodata,cart_qty=1)
                msg="Added to Cart"
                return render(request,"User/SearchProduct.html",{'msg':msg})
        else:
            tbl_booking.objects.create(user=custdata)
            bookingcount=tbl_booking.objects.filter(booking_status=0,user=custdata).count()
            if bookingcount>0:
                bookingdata=tbl_booking.objects.get(user=custdata,booking_status=0)
                cartcount=tbl_cart.objects.filter(booking=bookingdata,product=prodata).count()
                if cartcount>0:
                    msg="Already added"
                    return render(request,"User/SearchProduct.html",{'msg':msg})
                else:
                    tbl_cart.objects.create(booking=bookingdata,product=prodata,cart_qty=1)
                    msg="Added to Cart"
                    return render(request,"User/SearchProduct.html",{'msg':msg})
            else:
                msg="Added to Cart"
                return render(request,"User/SearchProduct.html",{'msg':msg})
    else:
        return redirect("webguest:Login")
    

def searchfood(request):
    if 'userid' in request.session:
        ar=[1,2,3,4,5]
        catObj=tbl_category.objects.all()
        fObj=tbl_food.objects.filter(shop__shop_vstatus=1)
        avg_list = []  # Create a list to store average ratings for each car
        reviewcount = 0
        for c in fObj:
            reviewcount = tbl_review.objects.filter(food=c.id).count()
        # print(reviewcount)
            res = 0
            avg = 0
            review = tbl_review.objects.filter(food=c.id)
            for rev in review:
                res = res + rev.user_rating
                # print(res)
                avg = res//reviewcount
                # print(avg)
            avg_list.append(avg)
        print(avg_list)
        cdata = zip(fObj,avg_list)
        return render(request,"User/SearchFood.html",{'data':cdata, 'datas':catObj, "avg": avg_list,"ar":ar})  
    else:
        return redirect("webguest:Login")

def ajax_food(request):
    subdata=tbl_subcategory.objects.get(id=request.GET.get('search'))
    shopdata=tbl_shop.objects.get(shop_vstatus=1)
    fObj=tbl_food.objects.filter(subc=subdata,shop=shopdata)
    return render(request,"User/AjaxFood.html",{'food':fObj})

def buyfood(request,fid):
    if 'userid' in request.session:
        fooddata=tbl_food.objects.get(id=fid)
        custdata=tbl_user.objects.get(id=request.session["userid"])
        bookingcount=tbl_booking.objects.filter(user=custdata,booking_status=0).count()
        if bookingcount>0:
            bookingdata=tbl_booking.objects.get(user=custdata,booking_status=0)
            cartcount=tbl_cart.objects.filter(booking=bookingdata,food=fooddata).count()
            if cartcount>0:
                msg="Already added"
                return render(request,"User/SearchFood.html",{'msg':msg})
            else:
                tbl_cart.objects.create(booking=bookingdata,food=fooddata,cart_qty=1)
                msg="Added to Cart!!"
                return render(request,"User/SearchFood.html",{'msg':msg})
        else:
            tbl_booking.objects.create(user=custdata)
            bookingcount=tbl_booking.objects.filter(booking_status=0,user=custdata).count()
            if bookingcount>0:
                bookingdata=tbl_booking.objects.get(user=custdata,booking_status=0)
                cartcount=tbl_cart.objects.filter(booking=bookingdata,food=fooddata).count()
                if cartcount>0:
                    msg="Already added"
                    return render(request,"User/SearchFood.html",{'msg':msg})
                else:
                    tbl_cart.objects.create(booking=bookingdata,food=fooddata,cart_qty=1)
                    msg="Added to Cart!!"
                    return render(request,"User/SearchFood.html",{'msg':msg})
            else:
                msg="Added to Cart!!"
                return render(request,"User/SearchFood.html",{'msg':msg})
    else:
        return redirect("webguest:Login")



def searchpet(request):
    if 'userid' in request.session:
        catObj=tbl_category.objects.all()
        shopdata=tbl_shop.objects.get(shop_vstatus=1)
        petsObj=tbl_pet.objects.filter(shop=shopdata)
        return render(request,"User/SearchPet.html",{'data':petsObj, 'datas':catObj}) 
    else:
        return redirect("webguest:Login")
 

def ajax_pet(request):
    if request.GET.get('search') != "":
        breeddata=tbl_breedtype.objects.get(id=request.GET.get('search'))
        shopdata=tbl_shop.objects.get(shop_vstatus=1)
        petsObj=tbl_pet.objects.filter(breedtype=breeddata,shop=shopdata)
        return render(request,"User/AjaxPet.html",{'pets':petsObj})
    elif request.GET.get('subcat') != "":
        breeddata=tbl_subcategory.objects.get(id=request.GET.get('subcat'))
        shopdata=tbl_shop.objects.get(shop_vstatus=1)
        petsObj=tbl_pet.objects.filter(breedtype__subcategory=breeddata,shop=shopdata)
        return render(request,"User/AjaxPet.html",{'pets':petsObj})
    else:
        breeddata=tbl_category.objects.get(id=request.GET.get('cat'))
        shopdata=tbl_shop.objects.get(shop_vstatus=1)
        petsObj=tbl_pet.objects.filter(breedtype__subcategory__category=breeddata,shop=shopdata)
        return render(request,"User/AjaxPet.html",{'pets':petsObj})

def buypet(request,petid):
    if 'userid' in request.session:
        petdata=tbl_pet.objects.get(id=petid)
        custdata=tbl_user.objects.get(id=request.session["userid"])
        bookingcount=tbl_booking.objects.filter(user=custdata,booking_status=0).count()
        if bookingcount>0:
            bookingdata=tbl_booking.objects.get(user=custdata,booking_status=0)
            cartcount=tbl_cart.objects.filter(booking=bookingdata,pet=petdata).count()
            if cartcount>0:
                msg="Already added"
                return render(request,"User/SearchPet.html",{'msg':msg})
            else:
                tbl_cart.objects.create(booking=bookingdata,pet=petdata,cart_qty=1)
                msg="Added to Cart"
                return render(request,"User/SearchPet.html",{'msg':msg})
        else:
            tbl_booking.objects.create(user=custdata)
            bookingcount=tbl_booking.objects.filter(booking_status=0,user=custdata).count()
            if bookingcount>0:
                bookingdata=tbl_booking.objects.get(user=custdata,booking_status=0)
                cartcount=tbl_cart.objects.filter(booking=bookingdata,pet=petdata).count()
                if cartcount>0:
                    msg="Already added"
                    return render(request,"User/SearchPet.html",{'msg':msg})
                else:
                    tbl_cart.objects.create(booking=bookingdata,pet=petdata,cart_qty=1)
                    msg="Added to Cart"
                    return render(request,"User/SearchPet.html",{'msg':msg})
            else:
                return render(request,"User/SearchPet.html")
    else:
        return redirect("webguest:Login")

def appointment(request,appid):
    if 'userid' in request.session:
        petObj=tbl_petdetails.objects.filter(user=request.session["userid"])
        if request.method=="POST":
            us=tbl_user.objects.get(id=request.session["userid"])
            pets=tbl_petdetails.objects.get(id=request.POST.get('sel_pet'))
            doc=tbl_doctor.objects.get(id=appid)
            tbl_appointment.objects.create(
                appointment_fordate=request.POST.get("txtdate"),
                appointment_fortime=request.POST.get("txttime"),
                pet=pets,
                doctor=doc,
                user=us)
            msg="Consultancy Appointment was successfully booked!"
            print(msg)
            return render(request,"User/AppointmentBooking.html",{'data':petObj,'msg':"Consultancy Appointment was successfully booked!"})
        else:
            return render(request,"User/AppointmentBooking.html",{'data':petObj})
    else:
        return redirect("webguest:Login")
    
def viewappointment(request):
    if 'userid' in request.session:
        appObj=tbl_appointment.objects.filter(user=request.session["userid"])
        return render(request,"User/ViewAppointment.html",{'data':appObj})
    else:
        return redirect("webguest:Login")

def cancelappointment(request,cid):
    tbl_appointment.objects.get(id=cid).delete()
    return redirect('webuser:UserHome')
      
def Mycart(request):
    if 'userid' in request.session:
        if request.method=="POST":
            bookingdata=tbl_booking.objects.get(id=request.session["bookingid"])
            bookingdata.totalamount=request.POST.get("carttotalamt")
            bookingdata.booking_status=1
            bookingdata.save()
            return redirect("webuser:Payment")
        else:
            customerdata=tbl_user.objects.get(id=request.session["userid"])
            bcount=tbl_booking.objects.filter(user=customerdata,booking_status=0).count()
        #cartcount=cart.objects.filter(booking__customer=customerdata,booking__status=0).count()
        if bcount>0:
            #cartdata=cart.objects.filter(booking__customer=customerdata,booking__status=0)
            book=tbl_booking.objects.get(user=customerdata,booking_status=0)
            bid=book.id
            request.session["bookingid"]=bid
            bkid=tbl_booking.objects.get(id=bid)
            pdt = tbl_product.objects.all()
            pdtdata=tbl_cart.objects.filter(booking=bkid,product__in=pdt)
            pet = tbl_pet.objects.all()
            petdata = tbl_cart.objects.filter(booking=bkid,pet__in=pet)
            food = tbl_food.objects.all()
            fooddata = tbl_cart.objects.filter(booking=bkid,food__in=food)
            return render(request,"User/MyCart.html",{'pet':petdata,"food":fooddata,"product":pdtdata})
        else:
            return render(request,"User/MyCart.html")
    else:
        return redirect("webguest:Login")
  
def DelCart(request,did):
    tbl_cart.objects.get(id=did).delete()
    return redirect("webuser:Cart")

def CartQty(request):
    qty=request.GET.get('QTY')
    cartid=request.GET.get('ALT')
    cartdata=tbl_cart.objects.get(id=cartid)
    cartdata.cart_qty=qty
    cartdata.save()
    return redirect("webuser:Cart")

def Payment(request):
    if 'userid' in request.session:
        bdata = tbl_booking.objects.filter(user_id=request.session["userid"], booking_status=1).order_by('-id').first()

        # bdata=tbl_booking.objects.get(id=request.session["userid"],booking_status=1)
        if request.method=="POST":
            bdata.payment_status=1
            bdata.save()
            return redirect("webuser:UserHome")
        else:
            return render(request,"User/Payment.html")
    else:
        return redirect("webguest:Login")
    


def viewbooking(request):
    if 'userid' in request.session:
        pdt = tbl_product.objects.all()
        petdata = tbl_pet.objects.all()
        fdata = tbl_food.objects.all()
        bdata = tbl_booking.objects.filter(user=request.session["userid"], booking_status=1)
        
        if bdata.exists():
            cartObj = tbl_cart.objects.filter(booking__in=bdata, product__in=pdt)
            cartpet = tbl_cart.objects.filter(booking__in=bdata, pet__in=petdata)
            cObj = tbl_cart.objects.filter(booking__in=bdata, food__in=fdata)
            return render(request, "User/MyBooking.html", {'data': cartObj, 'datafood': cObj, 'datapet': cartpet})
        else:
            return render(request, "User/MyBooking.html")
    else:
        return redirect("webguest:Login")


def cancelbooking(request,cartid):
    bdata=tbl_cart.objects.get(id=cartid)
    bdata.cart_status=5
    bdata.save()
    return redirect('webuser:UserHome')

def searchboard(request):
    if 'userid' in request.session:
        ar=[1,2,3,4,5]
        disObj=tbl_district.objects.all()
        boardObj=tbl_petboarding.objects.filter(boarding_status=1)
        avg_list = []  # Create a list to store average ratings for each car
        reviewcount = 0
        for c in boardObj:
            reviewcount = tbl_review.objects.filter(petboarding=c.id).count()
        # print(reviewcount)
            res = 0
            avg = 0
            review = tbl_review.objects.filter(petboarding=c.id)
            for rev in review:
                res = res + rev.user_rating
                # print(res)
                avg = res//reviewcount
                # print(avg)
            avg_list.append(avg)
        print(avg_list)
        cdata = zip(boardObj,avg_list)
        return render(request,"User/SearchPetBoarding.html",{'datas':cdata, 'disdata':disObj, "avg": avg_list,"ar":ar})  
    else:
        return redirect("webguest:Login")

def ajax_board(request):
    placedata=tbl_place.objects.get(id=request.GET.get('search'))
    boardObj=tbl_petboarding.objects.filter(place=placedata,boarding_status=1)
    return render(request,"User/AjaxBoarding.html",{'Board':boardObj})

def viewgrooming(request,vid):
    if 'userid' in request.session:
        boardObj=tbl_petboarding.objects.get(id=vid)
        groomdata=tbl_gdetails.objects.filter(boarding=boardObj)
        return render(request,"User/ViewGrooming.html",{'datas':groomdata, 'data':boardObj}) 
    else:
        return redirect("webguest:Login")

def bappointment(request,boardid):
    if 'userid' in request.session:
        if request.method=="POST":
            us=tbl_user.objects.get(id=request.session["userid"])
            board=tbl_petboarding.objects.get(id=boardid)
            tbl_boardingappointment.objects.create(
                board_fromdate=request.POST.get("txtdate"),
                board_todate=request.POST.get("txt_date"),
                board_details=request.POST.get("txtdetails"),
                boarding=board,
                user=us)
            return render(request,"User/PetBoardingAppointment.html")
        else:
            return render(request,"User/PetBoardingAppointment.html")
    else:
        return redirect("webguest:Login")
    
def viewbappointment(request):
    if 'userid' in request.session:
        bappObj=tbl_boardingappointment.objects.filter(user=request.session["userid"])
        print(bappObj)
        return render(request,"User/ViewPBAppointment.html",{'data':bappObj})
    else:
        return redirect("webguest:Login")
    
def viewgallery(request,gaid):
    if 'userid' in request.session:
        groomObj=tbl_gdetails.objects.get(id=gaid)
        gallery=tbl_gallery.objects.filter(gd=groomObj)
        return render(request,"User/ViewGallery.html",{'datas':gallery}) 
    else:
        return redirect("webguest:Login")

def gappointment(request,appid):
    if 'userid' in request.session:
        petObj=tbl_petdetails.objects.filter(user=request.session["userid"])
        if request.method=="POST":
            us=tbl_user.objects.get(id=request.session["userid"])
            pets=tbl_petdetails.objects.get(id=request.POST.get('sel_pet'))
            gdd=tbl_gdetails.objects.get(id=appid)
            board=tbl_petboarding.objects.get(id=appid)
            tbl_groomingappointment.objects.create(
                gappointment_fordate=request.POST.get("txtdate"),
                pet=pets,
                gd=gdd,
                user=us,
                boarding=board)
            return render(request,"User/GroomingAppointment.html", {'data':petObj})
        else:
            return render(request,"User/GroomingAppointment.html", {'data':petObj})
    else:
        return redirect("webguest:Login")
    
def viewgappointment(request):
    if 'userid' in request.session:
        gappObj=tbl_groomingappointment.objects.filter(user=request.session["userid"])
        return render(request,"User/ViewGroomAppointment.html",{'data':gappObj})
    else:
        return redirect("webguest:Login")


def chatpage(request,id):
    if 'userid' in request.session:
        doctor  = tbl_doctor.objects.get(id=id)
        return render(request,"User/Chat.html",{"doctor":doctor})
    else:
        return redirect("webguest:Login")

def ajaxchat(request):
    file = request.FILES.get("file")
    if file != '':
        if request.POST.get("msg") != '':
            from_user = tbl_user.objects.get(id=request.session["userid"])
            to_doctor = tbl_doctor.objects.get(id=request.POST.get("tid"))
            print(request.POST.get("tid"))
            tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user_from=from_user,doctor_to=to_doctor,chat_file=request.FILES.get("file"))
            return render(request,"User/Chat.html")
        else:
            from_user = tbl_user.objects.get(id=request.session["userid"])
            to_doctor = tbl_doctor.objects.get(id=request.POST.get("tid"))
            print(timezone.now())
            tbl_chat.objects.create(chat_content="",chat_time=datetime.now(),user_from=from_user,doctor_to=to_doctor,chat_file=request.FILES.get("file"))
            return render(request,"User/Chat.html")
    else:
        from_user = tbl_user.objects.get(id=request.session["userid"])
        to_doctor = tbl_doctor.objects.get(id=request.POST.get("tid"))
        # print(request.POST.get("tid"))
        print(timezone.now())
        tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user_from=from_user,doctor_to=to_doctor,chat_file="")
        return render(request,"User/Chat.html")
    
def ajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_user.objects.get(id=request.session["userid"])
    chat_data = tbl_chat.objects.filter((Q(user_from=user) | Q(user_to=user)) & (Q(doctor_from=tid) | Q(doctor_to=tid))).order_by('chat_time')
    return render(request,"User/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(user_from=request.session["userid"]) & Q(doctor_to=request.GET.get("tid")) | (Q(doctor_from=request.GET.get("tid")) & Q(user_to=request.session["userid"]))).delete()
    return render(request,"User/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})

#Product rating

def rating(request,cid):
    if 'userid' in request.session:
        parray=[1,2,3,4,5]
        cid=cid
        cdata=tbl_cart.objects.get(id=cid)
        productid=tbl_product.objects.get(id=cdata.product.id)
        wdata=tbl_user.objects.get(id=request.session["userid"])
        counts=0
        counts=stardata=tbl_review.objects.filter(product=productid).count()
        if counts>0:
            res=0
            stardata=tbl_review.objects.filter(product=productid).order_by('-review_datetime')
            for i in stardata:
                res = res + int(i.user_rating)
                avg=res//counts  
            return render(request,"User/Rating.html",{"cid":cid,"data":stardata,"ar":parray,"avg":avg,"count":counts})
        else:
            return render(request,"User/Rating.html",{'cid':cid})
    else:
        return redirect("webguest:login")

def ajaxrating(request):
    parray=[1,2,3,4,5]
    user_rating=request.GET.get('rating_data')
    user_name=request.GET.get('user_name')
    user_review=request.GET.get('user_review')
    cart=request.GET.get('workid')
    cdata=tbl_cart.objects.get(id=cart)
    productid=tbl_product.objects.get(id=cdata.product.id)
    print(productid)
    cust=tbl_user.objects.get(id=request.session["userid"])
    print(cust)
    tbl_review.objects.create(user_name=user_name,user_review=user_review,user_rating=user_rating,product=productid,user=cust)
    stardata=tbl_review.objects.filter(product=productid).order_by('-review_datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})

def starrating(request):
    r_len = 0
    five = four = three = two = one = 0
    car_id = request.GET.get("pdt")
    cdata = tbl_cart.objects.get(id=car_id)
    productid=tbl_product.objects.get(id=cdata.product.id)
    rate = tbl_review.objects.filter(product=productid)

    for i in rate:
        if int(i.user_rating) == 5:
            five += 1
        elif int(i.user_rating) == 4:
            four += 1
        elif int(i.user_rating) == 3:
            three += 1
        elif int(i.user_rating) == 2:
            two += 1
        elif int(i.user_rating) == 1:
            one += 1

        r_len += 1
    #print(r_len)

    rlen = r_len / 5
    #print(rlen)
    result = {"five": five, "four": four, "three": three, "two": two, "one": one, "total_review": rlen}
    return JsonResponse(result)

#food rating

def foodrating(request,cid):
    if 'userid' in request.session:
        parray=[1,2,3,4,5]
        cid=cid
        cdata=tbl_cart.objects.get(id=cid)
        productid=tbl_food.objects.get(id=cdata.food.id)
        wdata=tbl_user.objects.get(id=request.session["userid"])
        counts=0
        counts=stardata=tbl_review.objects.filter(food=productid).count()
        if counts>0:
            res=0
            stardata=tbl_review.objects.filter(food=productid).order_by('-review_datetime')
            for i in stardata:
                res = res + int(i.user_rating)
                avg=res//counts  
            return render(request,"User/RatingFood.html",{"cid":cid,"data":stardata,"ar":parray,"avg":avg,"count":counts})
        else:
            return render(request,"User/RatingFood.html",{'cid':cid})
    else:
        return redirect("webguest:login")

def ajaxfoodrating(request):
    parray=[1,2,3,4,5]
    user_rating=request.GET.get('rating_data')
    user_name=request.GET.get('user_name')
    user_review=request.GET.get('user_review')
    cart=request.GET.get('workid')
    cdata=tbl_cart.objects.get(id=cart)
    productid=tbl_food.objects.get(id=cdata.food.id)
    print(productid)
    cust=tbl_user.objects.get(id=request.session["userid"])
    print(cust)
    tbl_review.objects.create(user_name=user_name,user_review=user_review,user_rating=user_rating,food=productid,user=cust)
    stardata=tbl_review.objects.filter(food=productid).order_by('-review_datetime')
    return render(request,"User/AjaxRatingFood.html",{'data':stardata,'ar':parray})

def starfoodrating(request):
    r_len = 0
    five = four = three = two = one = 0
    car_id = request.GET.get("pdt")
    cdata = tbl_cart.objects.get(id=car_id)
    productid=tbl_food.objects.get(id=cdata.food.id)
    rate = tbl_review.objects.filter(food=productid)

    for i in rate:
        if int(i.user_rating) == 5:
            five += 1
        elif int(i.user_rating) == 4:
            four += 1
        elif int(i.user_rating) == 3:
            three += 1
        elif int(i.user_rating) == 2:
            two += 1
        elif int(i.user_rating) == 1:
            one += 1

        r_len += 1
    #print(r_len)

    rlen = r_len / 5
    #print(rlen)
    result = {"five": five, "four": four, "three": three, "two": two, "one": one, "total_review": rlen}
    return JsonResponse(result)

#boarding rating

def boardingrating(request,cid):
    if 'userid' in request.session:
        parray=[1,2,3,4,5]
        cid=cid
        cdata=tbl_petboarding.objects.get(id=cid)
        # productid=tbl_petboarding.objects.get(id=cdata.petboarding.id)
        wdata=tbl_user.objects.get(id=request.session["userid"])
        counts=0
        counts=stardata=tbl_review.objects.filter(petboarding=cdata).count()
        if counts>0:
            res=0
            stardata=tbl_review.objects.filter(petboarding=cdata).order_by('-review_datetime')
            for i in stardata:
                res = res + int(i.user_rating)
                avg=res//counts  
            return render(request,"User/RatingBoarding.html",{"cid":cid,"data":stardata,"ar":parray,"avg":avg,"count":counts})
        else:
            return render(request,"User/RatingBoarding.html",{'cid':cid})
    else:
        return redirect("webguest:login")

def ajaxboardingrating(request):
    parray=[1,2,3,4,5]
    user_rating=request.GET.get('rating_data')
    user_name=request.GET.get('user_name')
    user_review=request.GET.get('user_review')
    cart=request.GET.get('workid')
    cdata=tbl_petboarding.objects.get(id=cart)
    # productid=tbl_petboarding.objects.get(id=cdata.petboarding.id)
    # print(productid)
    cust=tbl_user.objects.get(id=request.session["userid"])
    print(cust)
    tbl_review.objects.create(user_name=user_name,user_review=user_review,user_rating=user_rating,petboarding=cdata,user=cust)
    stardata=tbl_review.objects.filter(petboarding=cdata).order_by('-review_datetime')
    return render(request,"User/AjaxRatingBoarding.html",{'data':stardata,'ar':parray})

def starboardingrating(request):
    r_len = 0
    five = four = three = two = one = 0
    car_id = request.GET.get("pdt")
    cdata = tbl_petboarding.objects.get(id=car_id)
    # productid=tbl_petboarding.objects.get(id=cdata.petboarding.id)
    rate = tbl_review.objects.filter(petboarding=cdata)

    for i in rate:
        if int(i.user_rating) == 5:
            five += 1
        elif int(i.user_rating) == 4:
            four += 1
        elif int(i.user_rating) == 3:
            three += 1
        elif int(i.user_rating) == 2:
            two += 1
        elif int(i.user_rating) == 1:
            one += 1

        r_len += 1
    #print(r_len)

    rlen = r_len / 5
    #print(rlen)
    result = {"five": five, "four": four, "three": three, "two": two, "one": one, "total_review": rlen}
    return JsonResponse(result)
