from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='auth_register'),
    path('login/', views.login, name='auth_login'),
    path('logout/', views.logout, name='auth_logout'),
    path('profile/', views.profile, name='auth_profile'),
]