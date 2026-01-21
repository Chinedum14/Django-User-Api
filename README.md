# Simple Django User API

A minimal Django REST API for user authentication with just the essentials.

## Features

- User registration (sign up)
- User authentication (sign in) 
- View user profile
- Token-based authentication

## API Endpoints

### Sign Up
- **URL:** `/api/signup/`
- **Method:** `POST`
- **Request:**
  ```json
  {
    "email": "user@example.com",
    "username": "username",
    "password": "password123",
    "password_confirm": "password123"
  }
  ```
- **Response:**
  ```json
  {
    "message": "User created successfully",
    "user": {
      "id": 1,
      "email": "user@example.com",
      "username": "username",
      "created_at": "2024-01-01T00:00:00Z"
    },
    "token": "your-auth-token-here"
  }
  ```

### Sign In
- **URL:** `/api/login/`
- **Method:** `POST`
- **Request:**
  ```json
  {
    "email": "user@example.com",
    "password": "password123"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Login successful",
    "user": {
      "id": 1,
      "email": "user@example.com",
      "username": "username",
      "created_at": "2024-01-01T00:00:00Z"
    },
    "token": "your-auth-token-here"
  }
  ```

### View Profile
- **URL:** `/api/profile/`
- **Method:** `GET`
- **Headers:** `Authorization: Token your-auth-token-here`
- **Response:**
  ```json
  {
    "message": "User profile retrieved successfully",
    "user": {
      "id": 1,
      "email": "user@example.com",
      "username": "username",
      "created_at": "2024-01-01T00:00:00Z"
    }
  }
  ```

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. Start server:
   ```bash
   python manage.py runserver
   ```

## Testing with Postman

1. **Sign up** - Create a new user
2. **Sign in** - Get authentication token
3. **View profile** - Use token in Authorization header

## Project Structure

```
django_user_api/
├── manage.py
├── requirements.txt
├── README.md
├── django_user_api/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── accounts/
    ├── models.py      # User model
    ├── serializers.py # Data validation
    ├── views.py       # API endpoints
    ├── urls.py        # URL routing
    └── admin.py       # Admin interface
```
