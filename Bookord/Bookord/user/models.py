from django.db import models

# Create your models here.

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.username, filename)

class User(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=16)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    profile_image = models.ImageField(upload_to=user_directory_path)
    age = models.PositiveIntegerField()
    gender = models.BooleanField()
    bio = models.TextField()
    friends = models.ManyToManyField('User')


    