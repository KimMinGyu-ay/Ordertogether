from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect
from .models import User
# Create your views here.
# 회원가입

def signup(request):

    if request.method == "POST":
        print(request.POST)
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]


        user = User.objects.create_user(
            username,
            password,
            email)
        user.last_name = lastname
        user.first_name = firstname 
        user.save()

        return redirect("user:login")
    return render(request, "accounts/signup.html")

# def signup(request):
#     if request.method == 'POST':
#         if request.POST['password1'] == request.POST['password2']:
#             user = User.objects.create_user(
#                                             username=request.POST['username'],
#                                             password=request.POST['password1'],
#                                             email=request.POST['email'],)
#             auth.login(request, user)
#             return redirect('/')
#         return render(request, 'signup.html')
#     return render(request, 'signup.html')


def login(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username = username, password = password)
        if user is not None: # 로그인 성공
            auth_login(request,user)
        else:
            print("실패")
    return render(request, "accounts/login.html")


def logout(request):
    auth_logout(request)
    return redirect ("user:login")