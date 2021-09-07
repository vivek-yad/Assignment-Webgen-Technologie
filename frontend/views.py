from django.http import request
from django.shortcuts import render,redirect
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse 
from api.serializers import TaskSerializer
# Create your views here.
from api.models import Task
import json
from django.contrib.auth.models import User,auth
# Create your views here.
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import Register
# Create your views here.



def index(request):
    return render(request,'index.html')



def register(request):
    if request.method=="POST":
        first=request.POST.get('firstname')
        last=request.POST.get('lastname')
        usern=request.POST.get('username')
        emaill=request.POST.get('email')
        passw=request.POST.get('password')
        confirmpass=request.POST.get('confirmpassword')
        user=Register(username=usern,firstname=first,lastname=last,email=emaill,password=passw,confirmpassword=confirmpass)
        user.save()
    return render(request,'register.html')



def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print(user)
            return redirect('list')
        else:
            messages.error(request,"Username or Password is Incorrect")
            return redirect('login')
    return render(request,'login.html')


def list(request):
    return render(request,'list.html')

def search_task(request):
    if request.method=='POST':
        search_str=json.loads(request.body).get('searchText')

        product=Task.objects.filter(
            product_id__starts_with=search_str
        )|Task.objects.filter(
            name__starts_with=search_str,
        )|Task.objects.filter(
            price__starts_with=search_str
        )|Task.objects.filter(
            Desc__icontains=search_str
        )
        data=product.values()
        return JsonResponse(list(data),safe=False)



# Create your views here.
