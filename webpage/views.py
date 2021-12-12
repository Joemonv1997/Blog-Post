from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import title
from django.contrib.auth.models import User,auth
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
    a=request.POST["username"]
    b=request.POST["password"]

    return render(request,"article.html",{'result':a})

def register_user(request):
    if request.method=="POST":
        a=request.POST["first"]
        b=request.POST["last"]
        c=request.POST["user"]
        d=request.POST["email"]
        e=request.POST["password"]
        f=request.POST["repeat_password"]
        user=User.objects.create_user(username=c,password=e,last_name=b,email=d,first_name=a)
        user.save()
        return redirect("/article")
    else:
        return render(request,"register.html")
