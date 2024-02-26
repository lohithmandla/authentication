from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.db import IntegrityError

User=get_user_model()

# Create your views here.
def login(request):
    return render(request,'login.html')
def validateemp(request):
     if request.method== 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            dbuser = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request,'login.html',{'error_message':'user not found'})
        user =authenticate(request,email=email,password=password)
        if user is not None:
            # return HttpResponse("Welcome")
            return render(request,'userdetails.html',{'user':user})
        else:
            return render(request,'login.html',{'error_message':'Invalid credentials'})
            
     else:
        return HttpResponse("invalid method")
     
def register(request):
    return render(request,'registration.html')

def saveuser(request):
    if request.method== 'POST':
        name=request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        print("sds")
        user=User(email=email,name=name)
        user.set_password(password)
        try:
            user.save()
        except IntegrityError as e:
            return render(request, 'registration.html', {'error_message': "Email must be unique"})
        return render(request,'registration.html',{'msg':'success'})
    else:
        return HttpResponse("invalid method")