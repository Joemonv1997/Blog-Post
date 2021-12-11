from django.urls import path
from . import views
urlpatterns=[
    path("",views.index,name="index"),
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
    path("article",views.main_page,name="main_page"),
    path("login_user",views.login_user,name="login_user"),
    path("register_user",views.register_user,name="register_user")
]