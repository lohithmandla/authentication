from django.urls import path
from authapp import views

urlpatterns = [
    path("",views.login,name='login') ,
    path("validateuser",views.validateemp,name='validateuser') ,
    path("register",views.register,name='registation') ,
    path("saveuser",views.saveuser,name='saveuser') ,

]