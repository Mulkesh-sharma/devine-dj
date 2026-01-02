from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER = 'user'
    ADMIN = 'admin'
    Pandit = 'pandit'

    ROLE_CHOICES = (
        (USER, 'User'),
        (ADMIN, 'Admin'),
        (Pandit, 'Pandit'),
    )

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default=USER
    )

def is_admin(self):
        return self.role == self.ADMIN

def is_pandit(self):
        return self.role == self.Pandit

def __str__(self):
        return self.username
