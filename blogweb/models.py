from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse


# Create your models here.
# Model for post
class Post(models.Model):
    title = models.CharField(max_length=100)
    title_tag = models.CharField(max_length=100, default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)
    publish_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' - ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')


# Model for Specific user
class ProfileUser(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_image = models.ImageField(null=True, blank=True, upload_to='images/profilepicture/')
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    linkedIn_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')
