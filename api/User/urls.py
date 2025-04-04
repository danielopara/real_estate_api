from api.user.views import create_user, get_user
from django.urls import path

urlpatterns = [
    path('create_user', create_user, name='create_user'),
    path('get_user', get_user, name='get_auth_user')
]
