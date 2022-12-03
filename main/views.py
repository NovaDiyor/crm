from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *


def error_view(request):
    return render(request, 'error.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        if user.count() > 0:
            usr = authenticate(username=username, password=password)
            if usr.status == 1:
                if usr is not None:
                    login(request, usr)
                    return redirect('dashboard')
                else:
                    return redirect('login')
            else:
                return redirect('login')
        else:
            return redirect('login')
    return render(request, 'login.html')


@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'dashboard.html')


@login_required(login_url='login')
def staff_view(request):
    context = {
        'staff': Staff.objects.all()
    }
    return render(request, 'staff.html', context)


@login_required(login_url='login')
def role_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Role.objects.create(name=name)
        return redirect('role')
    context = {
        'role': Role.objects.all()
    }
    return render(request, 'role.html', context)


@login_required(login_url='login')
def add_staff(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        status = request.POST.get('status')
        img = request.FILES.get('img')
        user = request.POST.get('user')
        time = request.POST.get('time')
        Staff.objects.create(name=name, status=status, img=img, user_id=user, time=time, many=0)
        return redirect('add-staff')
    context = {
        'user': User.objects.all()
    }
    return render(request, 'add-staff.html', context)


@login_required(login_url='login')
def category_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Category.objects.create(name=name)
        return redirect('category')
    context = {
        'category': Category.objects.all()
    }
    return render(request, 'category.html', context)

