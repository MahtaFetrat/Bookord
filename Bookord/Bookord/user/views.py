from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import User

# Create your views here.


def homepage_view(request):
    return render(request, 'user/homepage.html')


def index_view(request):
    return HttpResponseRedirect('login/')


def profile_view(request, username):
    user = get_object_or_404(User, pk=username)
    context = {
        'user': user,
        'header' : {
            'navbar_items': [{'title': 'FRIENDS', 'link': 'hi'}, {'title': 'BOOKS', 'link': 'hi'}, {'title': 'HOME', 'link': 'hi'}],
            'message' : 'welcome ' + user.first_name + ' :)',
            'cloud' : False
        }
    }
    return render(request, 'user/profile.html', context)


def login_view(request):
    return render(request, 'user/login.html')


def signup_view(request):
    return render(request, 'user/signup.html')
