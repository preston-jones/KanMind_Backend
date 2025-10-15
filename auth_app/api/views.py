# Standard library
from typing import Any

# Third-party
from django.contrib.auth import authenticate, get_user_model
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

# Local imports
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer

User = get_user_model()


class UserRegistrationView(CreateAPIView):
    """User registration endpoint."""
    
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
    
    def create(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        """Create user and return authentication token."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        
        return Response({
            'user_id': user.id,
            'username': user.username,
            'email': user.email,
            'token': token.key
        }, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    """User login endpoint."""
    
    permission_classes = [AllowAny]
    
    def post(self, request: Any) -> Response:
        """Authenticate user and return token."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        
        if user and user.is_active:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'user_id': user.id,
                'username': user.username,
                'token': token.key
            }, status=status.HTTP_200_OK)
        
        return Response({
            'error': 'Invalid credentials'
        }, status=status.HTTP_401_UNAUTHORIZED)


class UserLogoutView(APIView):
    """User logout endpoint."""
    
    permission_classes = [IsAuthenticated]
    
    def post(self, request: Any) -> Response:
        """Delete user token to logout."""
        try:
            request.user.auth_token.delete()
            return Response({
                'message': 'Successfully logged out'
            }, status=status.HTTP_200_OK)
        except Exception:
            return Response({
                'error': 'Error logging out'
            }, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(RetrieveAPIView):
    """Get authenticated user profile."""
    
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self) -> Any:
        """Return current authenticated user."""
        return self.request.user