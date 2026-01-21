# Import Django REST Framework serializers and authentication utilities
from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User


# Serializer for user registration (sign up)
# Handles validation and creation of new user accounts
class SignupSerializer(serializers.ModelSerializer):
    # Password field - write only so it doesn't get returned in responses
    password = serializers.CharField(write_only=True)
    
    # Password confirmation field to ensure passwords match
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        # Fields required for user registration
        fields = ('email', 'username', 'password', 'password_confirm')

    # Custom validation to ensure passwords match
    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("Passwords don't match")
        return attrs

    # Override create method to handle user creation
    def create(self, validated_data):
        # Remove password_confirm from validated data
        validated_data.pop('password_confirm')
        # Create user with Django's create_user method (handles password hashing)
        user = User.objects.create_user(**validated_data)
        return user


# Serializer for user login (sign in)
# Validates user credentials and returns authenticated user
class LoginSerializer(serializers.Serializer):
    # Email field for user identification
    email = serializers.EmailField()
    
    # Password field for authentication
    password = serializers.CharField()

    # Custom validation to authenticate user
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        # Ensure both email and password are provided
        if email and password:
            # Authenticate user using Django's authenticate function
            # Uses email as username since we configured USERNAME_FIELD = 'email'
            user = authenticate(username=email, password=password)
            if not user:
                raise serializers.ValidationError('Invalid credentials')
            # Store authenticated user in validated data
            attrs['user'] = user
            return attrs
        else:
            raise serializers.ValidationError('Must include email and password')


# Serializer for displaying user information
# Used to serialize user data for API responses
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # Fields to include in user profile responses
        fields = ('id', 'email', 'username', 'created_at')
        # Fields that should be read-only (cannot be updated via this serializer)
        read_only_fields = ('id', 'email', 'created_at')
