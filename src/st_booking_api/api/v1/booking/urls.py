from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet, AdminViewSet

router = DefaultRouter()
router.register(r'my_booking', BookingViewSet, basename='booking')
router.register(r'admin', AdminViewSet, basename='admin-booking')
urlpatterns = [
    path('', include(router.urls))

]