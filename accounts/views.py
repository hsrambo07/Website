from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method=='POST':
        #The user wants to signup
        if request.POST['password1'] == request.POST['password2']:
            try:
                user= User.objects.get(username=request.POST['username'])
                return render(request,'signup.html',{'error':'Username has already been taken'})
            except User.DoesNotExist:
                user= User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
    
        else:
            #The user wants to enter info
            return render(request,'signup.html',{'error':'Password dosent match'})
    else:
        return render(request,'signup.html')



def login(request):
    return render(request,'login.html')


def logout(request):
    # need to route to homepage
    return render(request,'logout.html')