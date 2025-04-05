from api.property.views import create_property, get_property, list_all_properties
from django.urls import path

urlpatterns = [
    path('create_property', create_property, name='create_property'),
    path('properties', list_all_properties, name="list_all_properties"),
    path('property', get_property, name="get_property")
]
