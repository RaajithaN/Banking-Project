from django.shortcuts import render, redirect
from .models import UserAccounts
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login
#from django.contrib import messages

# Create your views here.

def signup(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        #print(email)
        password = request.POST.get("psw")
        confirm_password = request.POST.get("psw-repeat")
        print(fname, lname, email,password,confirm_password)

        if password != confirm_password:
            return render(request,'user_accounts/signup.html', {
                "error":"Password and Confirm Password do not match"
            })
        
        if UserAccounts.objects.filter(email=email).exists():
               return render(request,'user_accounts/signup.html', {
                "error":"User with this email already exists"
            })
        
        #inserts data into database(fname, lname, pwd)
        UserAccounts.objects.create(
            first_name = fname,
            last_name = lname,
            email = email,
            password = password
         )


        send_mail(
             subject = "Welcome to my Bank",
             message = f"Hi {fname}, welcome to my bank. your username setup is successfull",
             from_email = settings.DEFAULT_FROM_EMAIL,
             recipient_list = [email]
            )
             

        return render(request,'user_accounts/signin.html')
    return render(request,'user_accounts/signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("psw")
        print(username, password)

        try:
           user = UserAccounts.objects.get(email=username, password=password)

            # ✅ Success message
            # messages.success(request, "Login successful! Welcome back.")
            
           return render(request,'user_accounts/signin.html', {
            "message":"Login successful! Welcome back."
            # return redirect('signin')  # or any page after login
        })

        except UserAccounts.DoesNotExist:
            return render(request,'user_accounts/signin.html', {
                "message":"Invalid email or password"
            #messages.error(request, "Invalid email or password")
            # return redirect('signin')
        })

    return render(request,'user_accounts/signin.html')

# def dashboard(request):
#     return render(request, 'user_accounts/dashboard.html'