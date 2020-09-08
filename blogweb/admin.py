from django.contrib import admin
from .models import Post, ProfileUser

# Register your models here.

# declare to register our models in superuser page
admin.site.register(Post)
admin.site.register(ProfileUser)
