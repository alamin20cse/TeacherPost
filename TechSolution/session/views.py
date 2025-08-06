from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def loginuser(request):
    if request.method=='POST':
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('homeview')
            else:
                messages.error(request, 'Invalid username or password')
        else:
                messages.error(request, 'Invalid username or password')
    else:
         form=AuthenticationForm()
    return render(request,'session/login.html',{'form':form})



def logoutuser(request):
    logout(request)
    messages.success(request,'succesfully logout ')
    return redirect('homeview')

from .forms import SignUpForm
def registration(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('session:login')
    else:
        form=SignUpForm()
    return render(request,'session/signup.html',{'form':form})


def change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,'password has changed succesfully')
            return redirect('homeview')
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request,'session/change_pass.html',{'form':form})


from .forms import UserProfileform
from .models import UserProfile
def userProfile(request):
    try:
        instance = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        instance = None

    if request.method == "POST":
        if instance:
            form = UserProfileform(request.POST, request.FILES, instance=instance)
        else:
            form = UserProfileform(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, "Successfully saved your profile")
            return redirect('homeview')  # Replace with your actual redirect target
    else:
        form = UserProfileform(instance=instance)
    context={
        'form':form
    }

    return render(request, 'session/user_profile_create.html', context)

def OwnerProfile(request):
    user=request.user
    return render(request,'session/userProfile.html',{'user':user})