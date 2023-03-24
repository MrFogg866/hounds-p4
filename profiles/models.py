from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth.models import User
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist


class CustomUser(AbstractUser):
    # custom fields and methods here
    groups = models.ManyToManyField(Group, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.user.username


def get_profile_by_username(username):
    Profile = apps.get_model('profiles', 'Profile')
    try:
        user = User.objects.get(username=username)
        return Profile.objects.get(user=user)
    except ObjectDoesNotExist:
        return None
