from django.urls import path
from .views import profile_view, admin_view, change_password, update_profile

app_name = 'profiles'

urlpatterns = [
    path('profile/<str:username>/', profile_view, name='profile'),
    path('change-password/', change_password, name='change_password'),
    path('update/<int:pk>/', update_profile, name='update_profile'),
    path('admin/', admin_view, name='admin'),
]
