# businessProfile/urls.py
from django.urls import path
from .views import BusinessProfileDetail, ServiceDetail, ServiceListCreate

urlpatterns = [
    path('business-profile/', BusinessProfileDetail.as_view(), name='business-profile-detail'),
    path('business-profile/services/', ServiceListCreate.as_view(), name='service-list-create'),
    path('services/<int:pk>/', ServiceDetail.as_view(), name='service-detail'),
]
