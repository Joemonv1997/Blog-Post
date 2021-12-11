from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,"home.html")
def register(request):
    return render(request,"register.html")
def login(request):
    return render(request,"login.html")
def main_page(request):
    return render(request,"article.html")

def login_user(request):
    a=request.POST["username"]
    b=request.POST["password"]

    return render(request,"article.html",{'result':a})

def register_user(request):
    a=request.POST["username"]
    b=request.POST["password"]

    return render(request,"article.html",{'result':a})
