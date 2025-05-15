from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
#from jumia.models import Product
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm



def student(request):
    return render(request,'student.html')

def login_user(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username , password=password)
        if user is not None: 
            login(request,user)
            messages.success(request,'You have logged in successfully...welcome!!')
            return redirect('jumia')
        else: 
            messages.success(request,'There was an error logging in...')
            return redirect('login')
    else:
        return render(request,'login_user.html')

def logout_user(request):   
    logout(request)
    messages.success(request,('Logout successful.....It was nice having you here'))
    return redirect('home')

def register_user(request):
    form=SignUpForm()
    if request.method=="POST":
        form=SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            username= form['username']
            password= form['password1']
            # authenticate user
            #log in user
            user=authenticate(username=username, password=password)
            messages.success(request,'welcome...you are now a new user!!')
            return render(request,'shop.html',{'form':form})
        else:
            messages.success(request,'there was an error...try again later')
            return redirect('jumia')
    else:
        return render(request,'register.html',{'form':form})