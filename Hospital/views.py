import datetime
from django.shortcuts import render,redirect
from Guest.models import*
from Hospital.models import*
from User.models import *
from django.db.models import Q
from datetime import datetime
from django.utils import timezone
from django.shortcuts import render, get_object_or_404


# Create your views here.

def HomePage(request):
    if 'hospitalid' in request.session:
        hospital_name=request.session["hname"]
        return render(request,"Hospital/HosHome.html",{'hospital':hospital_name})
    else:
        return redirect("webguest:Login")

def logout(request):
    if 'hospitalid' in request.session:
        del request.session["hospitalid"]
        return redirect("webguest:Main Index")
    else:
        return redirect("webguest:Login")

def myprofile(request):
    hospitalObj=tbl_hospital.objects.get(id=request.session["hospitalid"])
    return render(request,"Hospital/Profile.html",{'datas':hospitalObj})
    
def editprofile(request):
    hospitalObj=tbl_hospital.objects.get(id=request.session["hospitalid"])
    if request.method=="POST":
        hospitalObj.hospital_name=request.POST.get("txtname")
        hospitalObj.hospital_address=request.POST.get("txtadd")
        hospitalObj.hospital_contact=request.POST.get("txtno")
        hospitalObj.hospital_email=request.POST.get("txtemail")
        hospitalObj.save()
        return redirect('webhospital:Profile')
    else:
        return render(request,"Hospital/EditProfile.html",{'data':hospitalObj })
    
def password(request):
    if request.method=="POST":
        hos=tbl_hospital.objects.get(id=request.session["hospitalid"],hospital_password=request.POST.get("txt"))
        cpass=request.POST.get("txtconfirm")
        new=request.POST.get("txtnew")
        if cpass==new:
            hos.hospital_password=request.POST.get("txtconfirm")
            hos.save()
            msg="Password Updated!!"
            return render(request,"Hospital/ChangePass.html",{'msg':msg})
        else:
            msg="Password Mismatch!!"
            return render(request,"Hospital/ChangePass.html",{'msg':msg})
    else:
            return render(request,"Hospital/ChangePass.html")
        
def doctor(request):
    doctorObj=tbl_doctor.objects.filter(hospital=request.session["hospitalid"])
    if request.method=="POST":
        hos=tbl_hospital.objects.get(id=request.session["hospitalid"])
        tbl_doctor.objects.create(
            doctor_name=request.POST.get("txt_name"),
            doctor_contact=request.POST.get("txtcontact"),
            doctor_photo=request.FILES.get("filepic"),
            hospital=hos)
        return render(request,"Hospital/AddDoctor.html", {'data':doctorObj})
    else:
        return render(request,"Hospital/AddDoctor.html", {'data':doctorObj})
    
def deldoctor(request,did):
    tbl_doctor.objects.get(id=did).delete()
    return redirect('webhospital:Add Doctor')

def viewappointment(request):
    appObj=tbl_appointment.objects.filter(appointment_status=0)
    
    if request.method=="POST":
        return render(request,"Hospital/ViewUserAppointment.html",{'data':appObj})
    else:
        return render(request,"Hospital/ViewUserAppointment.html",{'data':appObj})
    
def acceptappointment(request, aid):
    appdata=tbl_appointment.objects.get(id=aid)
    appdata.appointment_status=1
    appdata.save()
    return redirect('webhospital:View User Appointment')
    
def rejectappointment(request, rid):
    appdata=tbl_appointment.objects.get(id=rid)
    appdata.appointment_status=2
    appdata.save()
    return redirect('webhospital:View User Appointment')

def Acceptedappointment(request):
    appObj=tbl_appointment.objects.filter(appointment_status=1)
    
    if request.method=="POST":
        return render(request,"Hospital/AcceptedAppointment.html",{'data':appObj})
    else:
        return render(request,"Hospital/AcceptedAppointment.html",{'data':appObj})
    
def Rejectedappointment(request):
    appObj=tbl_appointment.objects.filter(appointment_status=2)
    
    if request.method=="POST":
        return render(request,"Hospital/RejectedAppointment.html",{'data':appObj})
    else:
        return render(request,"Hospital/RejectedAppointment.html",{'data':appObj})
    
def viewdoctor(request):
    docdata=tbl_doctor.objects.filter(hospital=request.session["hospitalid"])
    return render(request,"Hospital/ViewDoctorsList.html",{'datas':docdata}) 
    
def view_user_chat(request, doctor_id):
    doctor = get_object_or_404(tbl_doctor, id=doctor_id)
    request.session["doctorid"]=doctor.id
    chat_users = tbl_chat.objects.filter(doctor_to=doctor).values('user_from').distinct()
    users = tbl_user.objects.filter(id__in=chat_users)

    return render(request, "Hospital/ViewUserChat.html", {'users': users, 'doctor': doctor})
# def viewuserchat(request,uid):
#     docdata=tbl_doctor.objects.get(id=uid)
#     chat=tbl_chat.objects.filter(doctor_to=docdata)
#     userObj = tbl_user.objects.get(id=chat.first().user_from.id)
#     if request.method=="POST":
#         return render(request,"Hospital/ViewUserChat.html",{'data':userObj})
#     else:
#         return render(request,"Hospital/ViewUserChat.html",{'data':userObj})
    
def chatpage(request,id):
    user  = tbl_user.objects.get(id=id)
    return render(request,"Hospital/Chat.html",{"user":user})

def ajaxchat(request):
    # print(request.POST.get("tid"))
    file = request.FILES.get("file")
    if file != '':
        if request.POST.get("msg") != '':
            from_doctor = tbl_doctor.objects.get(id=request.session["doctorid"])
            to_user = tbl_user.objects.get(id=request.POST.get("tid"))
            print(request.POST.get("tid"))
            tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),doctor_from=from_doctor,user_to=to_user,chat_file=request.FILES.get("file"))
            return render(request,"Hospital/Chat.html")
        else:
            from_doctor = tbl_doctor.objects.get(id=request.session["doctorid"])
            to_user = tbl_user.objects.get(id=request.POST.get("tid"))
            tbl_chat.objects.create(chat_content="",chat_time=datetime.now(),doctor_from=from_doctor,user_to=to_user,chat_file=request.FILES.get("file"))
            return render(request,"Hospital/Chat.html")
    else:
        from_doctor = tbl_doctor.objects.get(id=request.session["doctorid"])
        to_user = tbl_user.objects.get(id=request.POST.get("tid"))
        # print(request.POST.get("tid"))
        tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),doctor_from=from_doctor,user_to=to_user,chat_file="")
        return render(request,"Hospital/Chat.html")
    
def ajaxchatview(request):
    tid = request.GET.get("tid")
    doctor = tbl_doctor.objects.get(id=request.session["doctorid"])
    chat_data = tbl_chat.objects.filter((Q(doctor_from=doctor) | Q(doctor_to=doctor)) & (Q(user_from=tid) | Q(user_to=tid))).order_by('chat_time')
    return render(request,"Hospital/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(doctor_from=request.session["doctorid"]) & Q(user_to=request.GET.get("tid")) | (Q(user_from=request.GET.get("tid")) & Q(doctor_to=request.session["doctorid"]))).delete()
    return render(request,"Hospital/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})

def Vaccination(request, vaccid):
    petObj=tbl_petdetails.objects.get(id=vaccid)
    if request.method=="POST":
        petObj.pet_vaccinename=request.POST.get("txtname")
        petObj.pet_vaccinedate=request.POST.get("txtdate")
        petObj.save()
        msg="Vaccination Date Updated"
        return render(request,"Hospital/Vaccination.html",{'data':petObj,'msg':msg})
    else:
        return render(request,"Hospital/Vaccination.html",{'data':petObj })
