import uuid
from tabnanny import verbose

from django.contrib.auth.models import User
from django.db import models

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)
class UserAccount(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=False)
    dob = models.DateField(blank=False, null=False)
    other_names = models.CharField(max_length=255)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="user_account",
        to_field='username',
        db_column='user_username'
    )
    
    class Meta:
        verbose_name = "User Account"
        verbose_name_plural = "User Accounts"

    def __str__(self):
        return f"{self.first_name} {self.other_names} {self.last_name}" 

# Create your models here.
class Property(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=False)
    state = models.CharField(max_length=50, blank=False)
    city = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=250, blank=False)
    apartments = models.IntegerField( null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    owner = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name="owner")
    
    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"
    
    def __str__(self):
        return f"{self.name} - {self.owner.first_name} {self.owner.last_name}"
    
class Apartment(models.Model):
    RENT_STATUS_CHOICES = [
        ('available', 'available'),
        ('rented', 'rented'),
        ('maintenance', 'under maintenance')
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    rooms = models.IntegerField(null=False, blank=False)
    toilets = models.IntegerField(null=False, blank=False)
    bathrooms = models.IntegerField(null=False, blank=False)
    description = models.CharField(max_length=255)
    rent_status = models.CharField(max_length=20, choices=RENT_STATUS_CHOICES, default='available')
    apartment_number = models.IntegerField()
    
    class Meta:
        verbose_name = "Apartment"
        verbose_name_plural = "Apartments"
        
    def __str__(self):
        return f"{self.property.name} - Apartment {self.apartment_number}"
