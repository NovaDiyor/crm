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

