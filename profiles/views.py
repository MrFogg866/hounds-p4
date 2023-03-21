from django.shortcuts import render
from django.contrib.auth.models import User


def profile_view(request, username):
    user = User.objects.get(username=username)
    return render(request, 'profiles/profile.html', {'user': user})