# authApp/views.py

from rest_framework import generics
from authApp.models import User, CustomerProfile
from authApp.serializers import UserSerializer, CustomerProfileSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CustomerProfileCreateView(generics.CreateAPIView):
    queryset = CustomerProfile.objects.all()
    serializer_class = CustomerProfileSerializer

class LoginView(TokenObtainPairView):
    # Customize the token view if needed
    pass
