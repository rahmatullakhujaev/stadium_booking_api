from django.db import models
from st_booking_api.user.models import User
from st_booking_api.stadium.models import Stadium


class Booking(models.Model):
    status_choices = (
        (1, 'active'),
        (2, 'canceled'),
        (3, 'booked')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.SmallIntegerField(choices=status_choices, null=False, blank=False, default=1)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "%s - %s" % (self.user, self.stadium)
