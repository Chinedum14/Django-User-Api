# Import Django's path function for URL routing
from django.urls import path

# Import our API views from the same directory
from . import views


# URL patterns for the accounts app
# These define the API endpoints for user authentication
urlpatterns = [
    # User registration endpoint - POST /api/signup/
    path('signup/', views.signup, name='signup'),
    
    # User login endpoint - POST /api/login/
    path('login/', views.login, name='login'),
    
    # User profile endpoint - GET /api/profile/ (requires authentication)
    path('profile/', views.profile, name='profile'),
]
