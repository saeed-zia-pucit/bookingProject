from rest_framework import generics
from rest_framework.exceptions import ValidationError
from .models import BusinessProfile, Service
from .serializers import BusinessProfileSerializer, ServiceSerializer

class BusinessProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BusinessProfile.objects.all()
    serializer_class = BusinessProfileSerializer

    
class ServiceListCreate(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
