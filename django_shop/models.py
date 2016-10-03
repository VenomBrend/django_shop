from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    '''For extra user data'''
    user = models.OneToOneField(User, related_name='profile')
    phone = models.CharField(max_length=12, blank=True, default='')
    address = models.CharField(max_length=64, blank=True, default='')

    def __str__(self):
        return self.user.username
        