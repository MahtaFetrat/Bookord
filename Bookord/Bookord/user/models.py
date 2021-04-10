from django.db import models
from django.db.models.fields.related import ManyToManyField

# Create your models here.


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.username, filename)


def book_cover_path(instance, filename):
    return 'user_{0}/book_{1}/cover_{2}'.format(instance.owner.username, instance.id, filename)


def book_additional_path(instance, filename):
    return 'user_{0}/book_{1}/additional_{2}'.format(instance.owner.username, instance.id, filename)


class User(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=16)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80, blank=True)
    email = models.EmailField()
    profile_image = models.ImageField(
        upload_to=user_directory_path, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.BooleanField(null=True, blank=True)
    bio = models.TextField(blank=True)
    followings = models.ManyToManyField('User', null=True, blank=True)
    bookmarks = models.ManyToManyField('Book', null=True, blank=True)
    coins = models.PositiveBigIntegerField(default=0)


class Book(models.Model):
    title = models.CharField(max_length=200)
    owner = models.ForeignKey('User', on_delete=models.CASCADE)
    author_name = models.CharField(max_length=200)
    page_number = models.PositiveIntegerField()
    score = models.PositiveIntegerField(default=0)
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
