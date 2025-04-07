from api.apartment.views import (
    create_apartment,
    get_apartments,
    return_apartments,
    update_apartment,
)
from django.urls import path

urlpatterns = [
    path('create_apartment', create_apartment),
    path('property_apartments', return_apartments),
    path('update_apartment', update_apartment),
    path('get_apartments', get_apartments)
]
