from api.models import Apartment, Property, UserAccount
from django.contrib import admin

# Register your models here.
admin.site.register(UserAccount)
admin.site.register(Property)
admin.site.register(Apartment)