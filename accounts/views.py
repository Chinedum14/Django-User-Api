# Import Django REST Framework utilities for building API views
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# Import Token model for token-based authentication
from rest_framework.authtoken.models import Token

# Import our custom serializers for data validation
from .serializers import SignupSerializer, LoginSerializer, UserSerializer


# API view for user registration (sign up)
# Allows anyone to create a new account
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def signup(request):
    """
    Register a new user account.
    
    Expected data:
    {
        "email": "user@example.com",
        "username": "username",
        "password": "password123",
        "password_confirm": "password123"
    }
    """
    # Create serializer instance with request data
    serializer = SignupSerializer(data=request.data)
    
    # Validate the incoming data
    if serializer.is_valid():
        # Save the new user (serializer handles password hashing)
        user = serializer.save()
        
        # Create or get authentication token for the new user
        token, created = Token.objects.get_or_create(user=user)
        
        # Return success response with user data and token
        return Response({
            'message': 'User created successfully',
            'user': UserSerializer(user).data,
            'token': token.key
        }, status=status.HTTP_201_CREATED)
    
    # Return validation errors if data is invalid
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# API view for user login (sign in)
# Allows anyone to authenticate with email and password
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login(request):
    """
    Authenticate user and return authentication token.
    
    Expected data:
    {
        "email": "user@example.com",
        "password": "password123"
    }
    """
    # Create serializer instance with request data
    serializer = LoginSerializer(data=request.data)
    
    # Validate the credentials
    if serializer.is_valid():
        # Get authenticated user from serializer
        user = serializer.validated_data['user']
        
        # Create or get authentication token for the user
        token, created = Token.objects.get_or_create(user=user)
        
        # Return success response with user data and token
        return Response({
            'message': 'Login successful',
            'user': UserSerializer(user).data,
            'token': token.key
        }, status=status.HTTP_200_OK)
    
    # Return validation errors if credentials are invalid
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# API view for viewing user profile
# Requires authentication (valid token)
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def profile(request):
    """
    Get current user's profile information.
    
    Requires: Authorization: Token <token> header
    """
    # Serialize the authenticated user's data
    serializer = UserSerializer(request.user)
    
    # Return user profile data
    return Response({
        'message': 'User profile retrieved successfully',
        'user': serializer.data
    }, status=status.HTTP_200_OK)
