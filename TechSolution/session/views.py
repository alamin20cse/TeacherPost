from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm, UserProfileform
from .models import UserProfile

def loginuser(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homeview')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'session/login.html', {'form': form})

def logoutuser(request):
    logout(request)
    messages.success(request, 'Successfully logged out')
    return redirect('homeview')

def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Profile created automatically by signal
            return redirect('session:login')
    else:
        form = SignUpForm()
    return render(request, 'session/signup.html', {'form': form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password changed successfully')
            return redirect('homeview')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'session/change_pass.html', {'form': form})

def userProfile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = UserProfileform(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully saved your profile")
            return redirect('homeview')
    else:
        form = UserProfileform(instance=profile)
    return render(request, 'session/user_profile_create.html', {'form': form})

def OwnerProfile(request):
    return render(request, 'session/userProfile.html', {'user': request.user})
