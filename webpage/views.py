from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import title,Article
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .serializers import ArticleSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from webpage import serializers

def index(request):
    return render(request,"home.html")
def register(request):
    return render(request,"register.html")
def login(request):
    return render(request,"login.html")

@csrf_exempt
def main_page(request):
    if request.method=="GET":
        title_art=Article.objects.all()
        sa=ArticleSerializer(title_art,many=True)
        k=JSONRenderer().render(sa.data)
        # return render(request,"article.html",{'tit':k})
        return JsonResponse(sa.data,safe=False)
    elif request.method=="POST":
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors, status=400)

            # return render(request,"article.html",{'tit':data})
    else:
        title_art=Article.objects.all()
        sa=ArticleSerializer(title_art,many=True)
        k=JSONRenderer().render(sa.data)
        return render(request,"article.html",{'tit':k})


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