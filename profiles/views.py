from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .forms import UpdateProfileForm, CustomUserChangeForm
from .forms import UpdateProfileForm
from profiles.models import Profile

User = get_user_model()


@login_required
def profile_view(request, username, user=None):
    if user is None:
        user = get_object_or_404(User, username=username)
    context = {'user': user}
    return render(request, 'profiles/profile.html', context)


@login_required
@staff_member_required
def admin_view(request):
    users = User.objects.all()
    return render(request, 'profiles/admin.html', {'users': users})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been updated!')
            return redirect('profiles:profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'profiles/change_password.html', {'form': form})


@login_required
def update_profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profiles:profile', username=request.user.username)
    else:
        form = UpdateProfileForm(instance=profile)

    context = {
        'form': form,
        'user': request.user
    }

    return render(request, 'profiles/update_profile.html', context)




