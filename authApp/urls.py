# authApp/urls.py
from django.urls import path
from authApp.views import UserCreateView, CustomerProfileCreateView, LoginView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('register/profile/', CustomerProfileCreateView.as_view(), name='register_profile'),
    path('login/', LoginView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
