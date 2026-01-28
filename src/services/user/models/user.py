from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('customer', 'Customer'),
        ('vendor', 'Vendor'),
    ]

    email = models.EmailField(unique=True) 
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='customer')

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'role']

    def __str__(self):
        return f"{self.username} ({self.role})"