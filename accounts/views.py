from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth

def register(request):
    if request.method == 'POST':
        #Get form values
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password=request.POST['password']
        password2=request.POST['password2']
        email=request.POST['email']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email already used')
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password,email=email)
                    user.save()
                    messages.success(request,'User Registered')
                    return redirect('login')

        else:
            messages.error(request,'Password do not match')
            return redirect('register')


    else:
        return render(request, 'accounts/register.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        
        return redirect('index')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            context={
               'User':user
            }
            return render(request,'accounts/dashboard.html', context)
        else:
            messages.error(request, 'Invalid credentials')
            return redirect(login)

    else:
        return render(request, 'accounts/login.html')

