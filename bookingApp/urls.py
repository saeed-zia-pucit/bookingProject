# bookingApp/urls.py
from django.urls import path
from .views import BookingListCreate, BookingDetail

urlpatterns = [
    path('bookings/', BookingListCreate.as_view(), name='booking-list-create'),
    path('bookings/<int:pk>/', BookingDetail.as_view(), name='booking-detail'),
]