from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import User
from .forms import NameForm


# Create your views here.


def homepage_view(request):
    return render(request, 'user/homepage.html')


def index_view(request):
    return HttpResponseRedirect('/')


def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    context = {
        'user': user,
        'header': {
            'navbar_items': [{'title': 'FRIENDS', 'link': 'hi'}, {'title': 'BOOKS', 'link': 'hi'},
                             {'title': 'HOME', 'link': reverse('user:index')}],
            'message': 'welcome ' + user.first_name + ' :)',
            'cloud': False
        }
    }
    return render(request, 'user/profile.html', context)


def login_view(request):
    print(reverse('user:index'))
    context = {
        'header': {
            'navbar_items': [{'title': 'SIGNUP', 'link': '/user/signup'},
                             {'title': 'HOME', 'link': reverse('user:index')}]
        },
        'form_title': 'LOGIN',
        'style': {
            'color': 'black',
            'flip': False
        }
    }
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            ##
            return render(request, 'user/home.html')
        else:
            return render(request, 'user/home.html')
    else:
        form = NameForm()
        context['form'] = form
        return render(request, 'user/login.html', context)


def signup_view(request):
    context = {
        'header': {
            'navbar_items': [{'title': 'LOGIN', 'link': '/user/login'}, {'title': 'HOME', 'link': 'hi'}]
        },
        'form_title': 'SIGNUP',
        'style': {
            'color': '#002744',
            'flip': True
        }
    }
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            ##
            return render(request, 'user/home.html')
        else:
            return render(request, 'user/home.html')
    else:
        form = NameForm()
        context['form'] = form
        return render(request, 'user/login.html', context)
