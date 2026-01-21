# Import Django's built-in User model and database models
from django.contrib.auth.models import AbstractUser
from django.db import models


# Custom User model that extends Django's AbstractUser
# This allows us to use Django's built-in authentication features
# while adding our own custom fields
class User(AbstractUser):
    # Email field that must be unique - used as the main identifier
    email = models.EmailField(unique=True)
    
    # Timestamp for when the user account was created
    created_at = models.DateTimeField(auto_now_add=True)

    # Use email instead of username for authentication
    USERNAME_FIELD = 'email'
    
    # Required fields when creating a user (besides email and password)
    REQUIRED_FIELDS = ['username']

    # String representation of the User object
    def __str__(self):
        return self.email
