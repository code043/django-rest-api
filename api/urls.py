from django.urls import path
from .views import get_users, create_user, get_user, update_user, delete_user

urlpatterns = [
    path('users/', get_users, name='get_users'),
    path('users/create', create_user, name='create_user'),
    path('users/<int:pk>', get_user, name='get_user'),
    path('users/update/<int:pk>', update_user, name='update_user'),
    path('users/delete/<int:pk>', delete_user, name='delete_user')
]
