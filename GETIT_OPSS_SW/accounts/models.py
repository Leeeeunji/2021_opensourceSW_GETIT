from django.db import models
from django.contrib.auth.models import User, AbstractUser

class User(AbstractUser):
    name = models.TextField(max_length=200, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email = models.TextField(max_length=200, blank=True)
    phone = models.TextField(max_length=200, blank=True)