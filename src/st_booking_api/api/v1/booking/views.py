from rest_framework import viewsets, permissions
from st_booking_api.booking.models import Booking
from .serializers import BookingSerializer, BookingSerializerForStadiumOwner
from st_booking_api.api.v1.permission import IsStadiumOwner, AdminPermission, IsUser, IsAdminOrStadiumOwner


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class AdminViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializerForStadiumOwner

    def get_permissions(self):
        permissions_classes = [IsStadiumOwner]
        return [i() for i in permissions_classes]
