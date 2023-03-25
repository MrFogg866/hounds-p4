from django.urls import path
from .views import (profile_view, admin_view, change_password, 
                    update_profile, create_note, delete_note)

app_name = 'profiles'

urlpatterns = [
    path('profile/<str:username>/', profile_view, name='profile'),
    path('change-password/', change_password, name='change_password'),
    path('update/<str:username>/', update_profile, name='update_profile'),
    path('create/<str:username>/', create_note, name='create_note'),
    path('delete-note/<int:pk>/', delete_note, name='delete_note'),
    path('admin/', admin_view, name='admin'),
]
