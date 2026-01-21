# Import Django's admin module for admin interface configuration
from django.contrib import admin

# Import our custom User model
from .models import User

# Register the User model with Django admin
# This makes the User model visible and manageable in the admin interface
admin.site.register(User)
