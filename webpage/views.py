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
def add(request):
    a=int(request.GET["num1"])
    b=int(request.GET["num2"])
    add_r=a+b

    return render(request,"article_result.html",{'result':add_r})
