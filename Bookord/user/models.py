from django.contrib.auth.models import User
from django.db import models

from core.models import Book
# Create your models here.


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.username, filename)


class Profile(models.Model):
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]

    profile_image = models.ImageField(
        upload_to=user_directory_path, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=GENDER_MALE)
    bio = models.TextField(blank=True)
    following = models.ManyToManyField('Profile', blank=True, related_name='followers')
    bookmarks = models.ManyToManyField(Book, blank=True)
    coins = models.PositiveBigIntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')


