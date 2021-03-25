from django.db import models
from ..user.models import Book
from ..user.models import User

# Create your models here.

class Entry(models.Model):
    text = models.TextField()
    page_number = models.PositiveIntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

class Word(Entry):
    dictionary_entry = models.URLField(max_length=1000, default='https://www.ldoceonline.com/')
    mastry_score = models.PositiveIntegerField(default=0)

class Twitch(Entry):
    idea = models.TextField()
    liked = models.PositiveBigIntegerField(default=0)

class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)



