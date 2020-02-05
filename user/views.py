from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm 
from django.contrib import messages
from django.contrib.auth import authenticate,login as authorize,logout as deauth

# Create your views here.

def profile(request):
    if request.user.is_authenticated:
        return render(request,'user/profile.html')
    else:
        return HttpResponseRedirect('/user/login/')



def login(request):
    form=AuthenticationForm()
    if request.method=="POST":
        uname=request.POST['username']
        upass=request.POST['password']
        user=authenticate(username=uname,password=upass)
        if user.is_authenticated:
            authorize(request,user)
            return HttpResponseRedirect('/user/profile/')
        else:
            messages.info(request,"Username or password is not correct please try again")
            return HttpResponseRedirect('/user/login/')
    else:
        if request.user:
            return HttpResponseRedirect('/user/profile/')
        else:
            return render(request,'user/login.html',{'form':form})
             

    


def register(request):
    form=UserCreationForm()
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.INFO,"User is successfully created")
            return HttpResponseRedirect('/user/profile/')
    return render(request,'user/register.html',{'form':form})


def logout(request):
    if request.user.is_authenticated:
        deauth(request)
        messages.info(request,"You Successfully log out")
        form=AuthenticationForm()
        return render(request,'user/login.html',{'form':form}) 
        
    
    messages.info(request,'You Are not log in ')
    form=AuthenticationForm()
    return render(request,'user/login.html',{'form':form})   
