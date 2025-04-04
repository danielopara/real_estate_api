from api.user.views import create_user, get_user, list_users
from django.urls import path

urlpatterns = [
    path('create_user', create_user, name='create_user'),
    path('get_user', get_user, name='get_auth_user'),
    path('users', list_users, name='list all users')
]
