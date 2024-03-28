from django.shortcuts import render,redirect
from Guest.models import*
from Shop.models import*
from User.models import*

# Create your views here.

def HomePage(request):
    if 'shopid' in request.session:
        shopObj=tbl_shop.objects.get(id=request.session["shopid"])
        productObj=tbl_product.objects.filter(shop=request.session["shopid"])
        fObj=tbl_food.objects.filter(shop=request.session["shopid"])
        pObj=tbl_pet.objects.filter(shop=request.session["shopid"])
        shop_name=request.session["sname"]
        return render(request,"Shop/ShopHome.html",{'shop':shop_name,'shops':shopObj,'product':productObj,'pet':pObj,'food':fObj})
    else:
        return redirect("webguest:Login")
    
def logout(request):
    if 'shopid' in request.session:
        del request.session["shopid"]
        return redirect("webguest:Main Index")
    else:
        return redirect("webguest:Login")
    
def myprofile(request):
    if 'shopid' in request.session:
        shopObj=tbl_shop.objects.get(id=request.session["shopid"])
        return render(request,"Shop/Myprofile.html",{'datas':shopObj})
    else:
        return redirect("webguest:Login")
    
def editprofile(request):
    if 'shopid' in request.session:
        shopObj=tbl_shop.objects.get(id=request.session["shopid"])
        if request.method=="POST":
            shopObj.shop_name=request.POST.get("txtname")
            shopObj.shop_address=request.POST.get("txtadd")
            shopObj.shop_contact=request.POST.get("txtno")
            shopObj.shop_email=request.POST.get("txtemail")
            shopObj.save()
            return redirect('webshop:Profile')
        else:
            return render(request,"Shop/EditProfile.html",{'data':shopObj })
    else:
        return redirect("webguest:Login")
    
def password(request):
    if 'shopid' in request.session:
        if request.method=="POST":
            s=tbl_shop.objects.get(id=request.session["shopid"],shop_password=request.POST.get("txt"))
            cpass=request.POST.get("txtconfirm")
            new=request.POST.get("txtnew")
            if cpass==new:
                s.shop_password=request.POST.get("txtconfirm")
                s.save()
                msg="Password Changed.."
                return render(request,"Shop/ChangePass.html",{'msg':msg})
            else:
                msg="Password Mismatch!!"
                return render(request,"Shop/ChangePass.html",{'msg':msg})
        else:
                return render(request,"Shop/ChangePass.html")  
    else:
        return redirect("webguest:Login") 
    
def product(request):
    if 'shopid' in request.session:
        productObj=tbl_product.objects.filter(shop=request.session["shopid"])
        catObj=tbl_category.objects.all()
        if request.method=="POST":
            sp=tbl_shop.objects.get(id=request.session["shopid"])
            sub=tbl_subcategory.objects.get(id=request.POST.get('sel_sub'))
            tbl_product.objects.create(
                product_name=request.POST.get("txtname"),
                product_rate=request.POST.get("txtrate"),
                product_photo=request.FILES.get("filepic"),
                product_details=request.POST.get("txtdetails"),
                shop=sp,
                subc=sub)
            return render(request,"Shop/NewProduct.html", {'datas':catObj, 'data':productObj})
        else:
            return render(request,"Shop/NewProduct.html", {'datas':catObj, 'data':productObj})
    else:
        return redirect("webguest:Login")
    
def delproduct(request,did):
    tbl_product.objects.get(id=did).delete()
    return redirect('webshop:Product Details')

def editproduct(request,eid):
    product=tbl_product.objects.get(id=eid)
    catObj=tbl_category.objects.all()
    productObj=tbl_product.objects.filter(shop=request.session["shopid"])
    if request.method=="POST":
        product.product_name=request.POST.get("txtname")
        product.product_rate=request.POST.get("txtrate")
        product.product_photo=request.FILES.get("filepic")
        product.category_id=request.POST.get("sel_cat")
        product.product_details=request.POST.get("txtdetails")
        product.save()
        return redirect('webshop:Product Details')
    else:
        return render(request,"Shop/NewProduct.html", {'product':product,'datas':catObj, 'data':productObj})
def food(request):
    if 'shopid' in request.session:
        foodObj=tbl_food.objects.filter(shop=request.session["shopid"])
        catObj=tbl_category.objects.all()
        if request.method=="POST":
            sp=tbl_shop.objects.get(id=request.session["shopid"])
            sub=tbl_subcategory.objects.get(id=request.POST.get('sel_sub'))
            tbl_food.objects.create(
                company_name=request.POST.get("txtname"),
                food_rate=request.POST.get("txtrate"),
                food_photo=request.FILES.get("filepic"),
                food_content=request.POST.get("txtcontent"),
                shop=sp,
                subc=sub)
            return render(request,"Shop/NewFood.html", {'datas':catObj, 'data':foodObj})
        else:
            return render(request,"Shop/NewFood.html", {'datas':catObj, 'data':foodObj})       
    else:
        return redirect("webguest:Login")
        
def delfood(request,did):
    tbl_food.objects.get(id=did).delete()
    return redirect('webshop:Food Details')

def newpet(request):
    if 'shopid' in request.session:
        petObj=tbl_pet.objects.filter(shop=request.session["shopid"])
        catObj=tbl_category.objects.all()
        if request.method=="POST":
            sp=tbl_shop.objects.get(id=request.session["shopid"])
            btype=tbl_breedtype.objects.get(id=request.POST.get('sel_breed'))
            tbl_pet.objects.create(
                pet_dob=request.POST.get("txtdate"),
                pet_rate=request.POST.get("txtrate"),
                pet_photo=request.FILES.get("filepic"),
                pet_description=request.POST.get("txtcontent"),
                shop=sp,
                breedtype=btype)
            return render(request,"Shop/NewPet.html", {'datas':catObj, 'data':petObj})
        else:
            return render(request,"Shop/NewPet.html", {'datas':catObj, 'data':petObj})
    else:
        return redirect("webguest:Login")
    
def delpet(request,did):
    tbl_pet.objects.get(id=did).delete()
    return redirect('webshop:Pet Details')

def ajax_breedtype(request):
    subob=tbl_subcategory.objects.get(id=request.GET.get('sub'))
    breed=tbl_breedtype.objects.filter(subcategory=subob)
    return render(request,"Shop/AjaxBreed.html",{'su':breed})

def viewbooking(request):
    if 'shopid' in request.session:
        product = tbl_cart.objects.filter(product__shop=request.session["shopid"])
        food = tbl_cart.objects.filter(food__shop=request.session["shopid"])
        pet = tbl_cart.objects.filter(pet__shop=request.session["shopid"])
        all_pdt = set()
        for i in product:
            all_pdt.add(i.booking_id)
        for i in food:
            all_pdt.add(i.booking_id)
        for i in pet:
            all_pdt.add(i.booking_id)
        allbooking = tbl_booking.objects.filter(id__in=all_pdt)
        return render(request,"Shop/UserBooking.html",{"booking":allbooking})
    else:
        return redirect("webguest:Login")

def viewuserbooking(request,bid):
    if 'shopid' in request.session:
        pdt = tbl_product.objects.all()
        petdata = tbl_pet.objects.all()
        fdata = tbl_food.objects.all()
        # data=tbl_cart.objects.get(product__shop=request.session["shopid"])
        # bookingid=data.booking_id
        bdata=tbl_booking.objects.get(id=bid)
        # pdata=tbl_product.objects.filter(shop=request.session["shopid"])
        cartObj=tbl_cart.objects.filter(booking=bdata,product__in=pdt)
        foodObj=tbl_cart.objects.filter(booking=bdata,food__in=fdata)
        petObj=tbl_cart.objects.filter(booking=bdata,pet__in=petdata)
        print(petObj)
        return render(request,"Shop/UserProductBook.html",{'data':cartObj,'datafood':foodObj,'pet':petObj})
    else:
        return redirect("webguest:Login")
    

def packproduct(request, packid):
    cartdata=tbl_cart.objects.get(id=packid)
    cartdata.cart_status=1
    cartdata.save()
    return redirect('webshop:User_Booking')

def shipproduct(request, shipid):
    cartdata=tbl_cart.objects.get(id=shipid)
    cartdata.cart_status=2
    cartdata.save()
    return redirect('webshop:User_Booking')

def outproduct(request, outid):
    cartdata=tbl_cart.objects.get(id=outid)
    cartdata.cart_status=3
    cartdata.save()
    return redirect('webshop:User_Booking')

def deliproduct(request, delid):
    cartdata=tbl_cart.objects.get(id=delid)
    cartdata.cart_status=4
    cartdata.save()
    return redirect('webshop:User_Booking')