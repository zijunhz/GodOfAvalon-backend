from django.contrib import admin

# Register your models here.

from .models import Message, Room, User
admin.site.register(Room)
admin.site.register(User)
admin.site.register(Message)
