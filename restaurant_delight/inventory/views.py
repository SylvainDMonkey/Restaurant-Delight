from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

from .forms import NewUserForm


def sign_up_view(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('inventory:login')
        messages.error(request, "Unsuccesful information. Invalid information")
    form = NewUserForm()
    return render(request, 'registration/signup.html', context={"register_form":form})   


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password= password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect ('inventory:home')
            else:
                messages.error(request, "Invalid username or password")
    else:
        messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request, 'registration/login.html', context={"login_form":form})

def logout_view(request):
    logout(request)
    return redirect('inventory:login')


@login_required
def home(request):
    return render(request, "inventory/home.html")