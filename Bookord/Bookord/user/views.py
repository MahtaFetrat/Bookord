from django.http.response import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'user/home.html')

def index_view(request):
    return HttpResponseRedirect('login/')

def profile_view(request, username):
    return render(request, 'user/profile.html')

def login_view(request):
    return render(request, 'user/login.html')

def signup_view(request):
    return render(request, 'user/signup.html')
