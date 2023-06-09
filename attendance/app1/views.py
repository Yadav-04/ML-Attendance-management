from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse('Passwords do not match')
        elif pass1 == pass2:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')
    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=uname, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Invalid Credentials')

    return render(request, 'login.html')


def AdminLogin(request):
    # if request.method == 'POST':
    #     adminName = request.POST.get('aname')
    #     adminPass = request.POST.get('apass')
    #     print(adminName, adminPass)
    #     if adminName == 'admin' and adminPass == 'admin123':
    #         user = authenticate(request, username=adminName, password=adminPass)
    #         if user is not None:
    #             login(request, user)
    #             return redirect('ahome')
    #         else:
    #             return HttpResponse('Invalid Credentials')

    if request.method == 'POST':
        uname = request.POST.get('username')
        pass1 = request.POST.get('pass')
        print(uname,pass1)
        user = authenticate(request, username=uname, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('ahome')
        else:
            return HttpResponse('Invalid Credentials')

    return render(request, 'adminLogin.html')


def AdminHome(request):
    return render(request, 'adminHome.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')
