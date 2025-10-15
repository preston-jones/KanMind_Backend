# Standard library
from typing import Any

# Third-party
from django.urls import path

# Local imports
from .views import UserRegistrationView, UserLoginView, UserLogoutView, UserProfileView

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='user_registration'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
]