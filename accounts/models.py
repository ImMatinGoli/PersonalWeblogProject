from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    first_name = models.CharField()
    last_name = models.CharField()
    bio = models.TextField(blank=True, verbose_name="بیوگرافی", null=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name="تصویر پروفایل", default='avatars/default_avatar.png')

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name