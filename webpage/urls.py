from django.urls import path
from . import views
urlpatterns=[
    path("",views.index,name="index"),
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
    path("article",views.main_page,name="main_page"),
    path("login_user",views.login_user,name="login_user"),
    path("logout",views.logout,name="logout"),
    path("register_user",views.register_user,name="register_user"),
    path("article_detail/<int:pg_no>",views.article_detail,name="article_detail"),
    path("article_view",views.ArticleView.as_view(),name="article_view"),
    path("articledetail_view/<int:id>",views.ArticleDetailView.as_view(),name="articledetail_view"),
    path("article_generic",views.GenericAPIView.as_view(),name="article_generic")  
]