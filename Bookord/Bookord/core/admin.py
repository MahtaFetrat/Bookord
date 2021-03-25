from django.contrib import admin
from .models import Word
from .models import Twitch
from .models import Comment

# Register your models here.

admin.site.register(Word)
admin.site.register(Twitch)
admin.site.register(Comment)