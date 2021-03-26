from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import User

# Create your views here.


def home_view(request):
    return render(request, 'user/home.html')


def index_view(request):
    return HttpResponseRedirect('login/')


def profile_view(request, username):
    user = get_object_or_404(User, pk=username)
    context = {
        'user': user
    }
    return render(request, 'user/profile.html', context)


def login_view(request):
    return render(request, 'user/login.html')


def signup_view(request):
    return render(request, 'user/signup.html')
