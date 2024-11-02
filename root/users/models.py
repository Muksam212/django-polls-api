from django.db import models

from root.utils import BaseModel
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
# Create your models here.

class User(AbstractUser, BaseModel):
    username = models.CharField(max_length=100, unique = True)
    email = models.EmailField(unique = True)
    full_name = models.CharField(max_length=100, null = True, blank = False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email}"