from django.http import request
from django.shortcuts import redirect, render
from accounts.models import User
from django.contrib import auth

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user=User.objects.create_user(
                username = request.POST['user-username'],
                name = request.POST['name'],
                password=request.POST['password1'],
                birth_date = request.POST['birth_date'],
                email = request.POST['email'],
                phone = request.POST['phone'])
            auth.login(request,user)
            return redirect('/main')
    return render(request, 'signup.html')

def login_request(request):
    if request.method == "POST":
        username = request.POST['user-username']
        password=request.POST['password1']
        user=auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/main')
        else:
            return render(request,'login.html', {'error':'username or password is incorrect'})
    else:
        return render(request, 'login.html')

def logout_request(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')
    return redirect('/')