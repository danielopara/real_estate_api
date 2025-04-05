from api.property.views import create_property
from django.urls import path

urlpatterns = [
    path('create_property', create_property, name='create_property')
]
