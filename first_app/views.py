from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import CostumerRegistration
# Create your views here.

def registration(request):
    qs = CostumerRegistration.objects.all()
    lid = [i.id for i in qs]
    try:
        id = (lid[-1] + 1)
    except IndexError:
        id = 101
    name = request.POST["name"]
    num = request.POST["number"]
    if len(num) == 10:
        phone = num
    else:
        p = 'Phone number should be 10 digits,you given {}'.format(len(num))
        return render(request, 'register.html', {'phonedata': p})
    mail = request.POST['email']
    address = request.POST["add"]
    pwd1 = request.POST["pass1"]
    pwd2 = request.POST["pass2"]
    if pwd1 == pwd2:
        password = pwd1
    else:
        return render(request,'register.html',{'data':'Password and Re enter Password should be same'})
    CostumerRegistration(id = id,name=name,number=phone,email=mail
                         ,address=address,pwd=password).save()
    return render(request,'welcome.html',{'data':name})

def checkuser(req):
    id = req.POST["id"]
    password = req.POST["pwd"]
    qs = CostumerRegistration.objects.get(email=id)
    if id == qs.email and password == qs.pwd:
        req.session['user_name'] = qs.name
        if req.session.has_key('user_name'):
            return render(req,'welcome.html',{'logindata':qs.name})
    else:
        return render(req,'index.html',{"data":"username and password doesnt match"})

def userlogout(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return redirect('login')

from .sms import sendSMS
def forgotpassword(request):
    phone = request.POST["phone_number"]
    try:
        qs = CostumerRegistration.objects.get(number=phone)
        request.session["user_username"] = qs.name
        mess ="Hello{}! \n Here is your Information: \n user name:{}\n Password : {}".format(qs.name,qs.email,qs.pwd)
        x=sendSMS(str(phone),mess)
        messages.success(request, "Your Credentials sent to your registered mobile number if your not mobile number not in DND list")
        print(x)
        del request.session["user_username"]
        return redirect("login")
    except CostumerRegistration.DoesNotExist:
        return render(request,'forgotpwd.html',{'pwd_data':"given mobile number does not exist in our database"})
