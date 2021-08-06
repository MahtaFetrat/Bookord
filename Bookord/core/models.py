from django.contrib.auth.models import User
from django.db import models


# Create your models here.

def book_cover_path(instance, filename):
    return 'user_{0}/book_{1}/cover_{2}'.format(instance.owner.username, instance.id, filename)


def book_additional_path(instance, filename):
    return 'user_{0}/book_{1}/additional_{2}'.format(instance.owner.username, instance.id, filename)


class Book(models.Model):
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=200)
    page_number = models.PositiveIntegerField()
    additional_info = models.TextField(blank=True)
    overview = models.TextField(blank=True)
    cover_image = models.ImageField(
        upload_to=book_cover_path, null=True, blank=True)
    additional_image_1 = models.ImageField(
        upload_to=book_additional_path, null=True, blank=True)
    additional_image_2 = models.ImageField(
        upload_to=book_additional_path, null=True, blank=True)
    additional_image_3 = models.ImageField(
        upload_to=book_additional_path, null=True, blank=True)
    #
    # class Meta:
    #     ordering = ['']


class Entry(models.Model):
    text = models.TextField()
    page_number = models.PositiveIntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class Word(Entry):
    dictionary_entry = models.URLField(max_length=1000, default='https://www.ldoceonline.com/')
    mastery_score = models.PositiveIntegerField(default=0)


class Twitch(Entry):
    idea = models.TextField()
    liked = models.PositiveBigIntegerField(default=0)


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
