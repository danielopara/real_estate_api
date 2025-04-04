from api.auth.views import login_user
from django.urls import path

urlpatterns = [
    path('login', login_user, name='login_user')
]
