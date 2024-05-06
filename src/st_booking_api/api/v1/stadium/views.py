from rest_framework import viewsets, permissions
from st_booking_api.api.v1.permission import AdminPermission, IsStadiumOwner, IsAdminOrStadiumOwner
from st_booking_api.stadium.models import Stadium, StadiumImage
from .serializer import StadiumSerializer, StadiumImageSerializer
from st_booking_api.booking.models import Booking
from django.db.models import Q
from math import asin, cos, sqrt, sin, radians


class StadiumViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrStadiumOwner]
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsAdminOrStadiumOwner]
        return [i() for i in permission_classes]

    # def perform_create(self, serializer):
    #     pass

    def haversine(self, lat1, lon1, lat2, lon2):

        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6371
        return c * r
    def list(self, request, *args, **kwargs):
        start_time = request.query_params.get("start_time")
        end_time = request.query_params.get("end_time")
        lat = request.query_params.get("lat")
        lon = request.query_params.get("lon")

        if start_time and end_time:
            self.queryset = Stadium.objects.exclude(
                id__in = Booking.objects.filter(
                    Q(start_time__lte=start_time, end_time__gte=end_time) |
                    Q(start_time__gte = start_time, start_time__lte = end_time) |
                    Q(end_time__gte=start_time, end_time__lte=end_time),
                    status = 1
                ).values_list('stadium_id', flat=True)
            )
        if lat and lon:
            user_location = (float(lat), float(lon))
            for stadium in self.queryset:
                stadium_location = (stadium.lat, stadium.lon)
                distance = self.haversine(*user_location, *stadium_location)
                print("distance", distance)
                setattr(stadium, 'distance', distance)

            self.queryset = sorted(self.queryset, key=lambda x:x.distance)
        return super().list(request, *args, **kwargs)



class StadiumImageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrStadiumOwner]
    queryset = StadiumImage.objects.all()
    serializer_class = StadiumImageSerializer