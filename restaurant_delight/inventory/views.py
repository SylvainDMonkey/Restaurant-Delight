from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect

def login_view(request):
    context = {
    "login_view": "active"
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inventory:home')
        else:
            return HttpResponse('Erreur message')
    return render(request, 'registration/login.html', context)


def home(request):
    context = {"name": request.user}
    return render(request, "inventory/home.html", context)