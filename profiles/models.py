from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth.models import User
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUser(AbstractUser):
    # custom fields and methods here
    groups = models.ManyToManyField(Group, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    dog_name = models.CharField(max_length=50, blank=True)
    dog_breed = models.CharField(max_length=50, blank=True)
    dog_allergies = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def get_profile_by_username(username):
    Profile = apps.get_model('profiles', 'Profile')
    try:
        user = User.objects.get(username=username)
        return Profile.objects.get(user=user)
    except ObjectDoesNotExist:
        return None
