from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

# Create your views here.
from .models import Book


def index_view(request, username, book_id):
    return HttpResponseRedirect('aphorism/')


def aphorism_view(request, username, book_id):
    book = get_object_or_404(Book, pk=book_id)
    context = {
        'book': book
    }
    return render(request, 'core/aphorism.html', context)


def language_view(request, username, book_id):
    return render(request, 'core/language.html')


def review_view(request, username, book_id):
    return render(request, 'core/review.html')


def newbook_view(request, username):
    return render(request, 'core/newbook.html')
