from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def index_view(request):
    return HttpResponseRedirect('aphorism/')

def aphorism_view(request, username, book_id):
    return render(request, 'core/aphorism.html')

def language_view(request, username, book_id):
    return render(request, 'core/language.html')

def review_view(request, username, book_id):
    return render(request, 'core/review.html')

def newbook_view(request, username):
    return render(request, 'core/newbook.html')