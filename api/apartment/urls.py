from api.apartment.views import create_apartment
from django.urls import path

urlpatterns = [
    path('create_apartment', create_apartment)
]
