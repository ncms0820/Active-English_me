from django.db import models
from core import models as core_models


class Reservation(core_models.TimeStampedModel):

    """Reservation Model Definition """

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled"),
    )

    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING
    )
    start_date = models.DateField()
    end_date = models.DateField()
    student = models.ForeignKey(
        "users.User", related_name="reservations", on_delete=models.CASCADE
    )
    lecture = models.ForeignKey(
        "lectures.Lecture", related_name="reservations", on_delete=models.CASCADE
    )
