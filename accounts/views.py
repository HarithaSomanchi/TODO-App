from email import message
from django.shortcuts import redirect, render,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User ,auth

# Create your views here.
def register(request):
    if request.method == "POST":
        username=request.POST["username"]
        password=request.POST["password"]
        email=request.POST["email"]
        if User.objects.filter(username = username).exists():
            messages.info(request,'user name taken')
            return redirect('register') 
        user=User.objects.create_user(username =username, password= password, email=email)
        user.save()
        return redirect('login')  
    else:
        return render(request,"register.html")
def Login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user = auth.authenticate(username=username , password =password)
        if user is not None:
            auth.login(request,user)
            return render(request,"home.html")
        else:
            messages.info(request , "Invalid Credinteails")
            return redirect('login')   
    else:
        return render(request,'login.html')
def Logout(request):
    auth.logout(request)
    return redirect('todoapp')
    
