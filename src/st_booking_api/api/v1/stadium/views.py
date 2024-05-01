from rest_framework import viewsets
from st_booking_api.api.v1.permission import AdminPermission, IsStadiumOwner
from st_booking_api.stadium.models import Stadium, StadiumImage
from .serializer import StadiumSerializer, StadiumImageSerializer


class StadiumViewSet(viewsets.ModelViewSet):
    permission_classes = [AdminPermission, IsStadiumOwner]
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer


class StadiumImageViewSet(viewsets.ModelViewSet):
    permission_classes = [AdminPermission, IsStadiumOwner]
    queryset = StadiumImage.objects.all()
    serializer_class = StadiumImageSerializer