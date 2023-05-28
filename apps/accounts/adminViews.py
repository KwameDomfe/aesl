from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse

#ADMIN LOGIN
def admin_Home(request):
    context = {}
    return render(request,'accounts/admin-templates/admin-home.html', context)

def admin_Login(request):

    username=request.POST.get('username')
    password=request.POST.get('password')
    print(username,password)

    user=authenticate(
        request=request, 
        username=username, 
        password=password,
    )
    print(user)
    
    if user is not None:
        login(request=request, user=user)
        return HttpResponseRedirect(reverse('admin-login'))
    else:
        messages.error(request, 'Invalid Credentials')
        return HttpResponseRedirect(reverse('accounts:admin-home'))

def admin_logout(request):
    if request.method =='POST':
        logout(request)
        return redirect('/accounts/user-login')
    context = {}
    return render(request,'accounts/user-logout.html', context)
