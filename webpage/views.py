from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import title
from django.contrib.auth.models import User,auth
from django.contrib import messages
def index(request):
    return render(request,"home.html")
def register(request):
    return render(request,"register.html")
def login(request):
    return render(request,"login.html")
def main_page(request):
    title_art=title.objects.all()
    return render(request,"article.html",{'tit':title_art})

def login_user(request):
    if request.method=="POST":
        a=request.POST["username"]
        b=request.POST["password"]
        user=auth.authenticate(username=a,password=b)
        if user is not None:
            auth.login(request,user)
            return redirect("/article")
        else:
            messages.info(request,"Wrong Username or Password")
            return render(request,"login.html")
    else:
        return render(request,"login.html")

def register_user(request):
    if request.method=="POST":
        a=request.POST["first"]
        b=request.POST["last"]
        c=request.POST["user"]
        d=request.POST["email"]
        e=request.POST["password"]
        f=request.POST["repeat_password"]
        if e!=f:
            messages.info(request,"Password Not Match")
            return render(request,"register.html")
        elif User.objects.filter(username=c).exists():
            messages.info(request,"Username Taken")
            return render(request,"register.html")
        elif User.objects.filter(email=d).exists():
            messages.info(request,"Email Already exist")
            return render(request,"register.html")
        else:
            user=User.objects.create_user(username=c,password=e,last_name=b,email=d,first_name=a)
            user.save()
            return redirect("/article")
    else:
        return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect("/")