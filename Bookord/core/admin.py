from django.contrib import admin
from .models import Word, Book, Twitch, Comment

# Register your models here.

admin.site.register(Word)
admin.site.register(Twitch)
admin.site.register(Comment)
admin.site.register(Book)
