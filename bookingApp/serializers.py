from rest_framework import serializers

from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'service_name', 'date', 'time_slot']