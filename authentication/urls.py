from django.urls import path
from . import views



urlpatterns = [
    path('', views.home , name="home"),
    path('signup',views.signup,name="Signup"),
    path('signin',views.signin,name="Signin"),
    path('signout',views.signout,name="Signout"),
    path('login',views.login,name="Login"),
   
]

