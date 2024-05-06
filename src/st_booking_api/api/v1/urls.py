from django.urls import path, include
from .booking import urls as booking_urls
from .stadium import urls as stadium_urls
from .user import urls as user_urls

urlpatterns = [
    path('booking/', include(booking_urls)),
    path('stadium/', include(stadium_urls)),
    path('user/', include(user_urls)),
]