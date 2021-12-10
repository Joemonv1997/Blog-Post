from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Welcome to the app")
def register(request):
    return HttpResponse("Welcome to the Register Page")
def login(request):
    return HttpResponse("Welcome to the Login Page")
def main_page(request):
    return HttpResponse("Welcome to the Main Page")
