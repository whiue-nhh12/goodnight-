from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
def login_view(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,"login.html",{'error':'Tai khoan khong ton tai'})
    return render(request,'login.html')
@login_required
def home(request):
    return render(request,'home.html')
@login_required
def ngungon1(request):
    return render(request,'ngungon1.html')
@login_required
def ngungon2(request):
    return render(request,'ngungon2.html')
@login_required
def ngungon3(request):
    return render(request,'ngungon3.html')
@login_required
def ngungon4(request):
    return render(request,'ngungon4.html')
@login_required
def ngungon5(request):
    return render(request,'ngungon5.html')
@login_required
def ngungon6(request):
    return render(request,'ngungon6.html')
@login_required
def ngungon7(request):
    return render(request,'ngungon7.html')

@login_required
def ngungon_8_3(request):
    return render(request,'ngungon_8_3.html')