import uuid

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Property(models.Model):
    id = models.UUIDField(default = uuid.uuid4, editable=False)
