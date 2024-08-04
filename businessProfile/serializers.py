from rest_framework import serializers
from .models import BusinessProfile, Service

class BusinessProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessProfile
        fields = ['id', 'first_name', 'last_name', 'email', 'bio']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'price', 'duration']  # Exclude 'business' from writable fields

