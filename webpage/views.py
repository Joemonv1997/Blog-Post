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
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from webpage import serializers
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
def index(request):
    return render(request,"home.html")
def register(request):
    return render(request,"register.html")
def login(request):
    return render(request,"login.html")

@api_view(["GET","POST"])
def main_page(request):
    if request.method=="GET":
        title_art=Article.objects.all()
        sa=ArticleSerializer(title_art,many=True)
        k=JSONRenderer().render(sa.data)
        # return render(request,"article.html",{'tit':k})
        return Response(sa.data)
    elif request.method=="POST":
        serializer = ArticleSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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


@api_view(["GET","PUT","DELETE"])
def article_detail(request,pg_no):
    try:
        title_art=Article.objects.get(pk=pg_no)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        serializer = ArticleSerializer(title_art)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    elif request.method=="PUT":
        serializer = ArticleSerializer(title_art,request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        title_art.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ArticleView(APIView):
    def get(self,request):
        title_art=Article.objects.all()
        sa=ArticleSerializer(title_art,many=True)
        k=JSONRenderer().render(sa.data)
        return Response(sa.data)
    def post(self,request):
        serializer = ArticleSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetailView(APIView):
    def get_object(self,id):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self,request,id):
        title_art=self.get_object(id)
        serializer = ArticleSerializer(title_art)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def put(self,request,id):
        title_art=self.get_object(id)
        serializer = ArticleSerializer(title_art,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        title_art=self.get_object(id)
        title_art.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GenericAPIView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):   
    serializer_class =ArticleSerializer
    queryset=Article.objects.all()
    def get(self,request):
        return self.list(request)
    def post(self, request):
        return self.create(request)
    