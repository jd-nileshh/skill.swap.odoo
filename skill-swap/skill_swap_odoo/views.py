from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.conf import settings
from swaps.models import SwapUser
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home(request):
    data=SwapUser.objects.all()
    return render(request,'home.html',{'data':data})

def sign_up(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
        city = request.POST['city']
        profile = request.FILES['profile']  # Changed from POST to FILES
        skills = request.POST['skills']
        skills_wanted = request.POST['skills_wanted']
        is_public = request.POST.get('is_public') == 'on'  # Handle checkbox
        
        user = SwapUser.objects.create_user(
            username=username,
            password=password,
            name=name,
            city=city,
            profile=profile,
            skills=skills,
            skills_wanted=skills_wanted,
            is_public=is_public
        )
        return redirect('login_view')
    
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # or any other route name
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')
