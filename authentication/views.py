from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUsersForm

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ('Error Logging In.'))
            return redirect('login')
    else: 
        return render(request, 'authentication/login.html', {})
    
def user_logout(request):
    logout(request)
    messages.success(request, ('Logged out.'))
    return redirect('login')

def user_register(request):
    if request.method == 'POST':
        form = RegisterUsersForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate( username=username, password=password)
            login(request, user)
            messages.success(request, ('Registered.'))
            return redirect('login')
    else:
        form = RegisterUsersForm()

    return render(request, 'authentication/register.html', {'form': form})

