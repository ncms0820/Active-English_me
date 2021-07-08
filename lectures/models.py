from django.db import models
from core import models as core_models
# Create your models here.


class Lecture(core_models.TimeStampedModel):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    teacher = models.ForeignKey(
        "users.User", related_name="lectures", on_delete=models.CASCADE)
    limit = models.IntegerField()


class ActiveLecture(core_models.TimeStampedModel):
    lecture = models.ForeignKey(
        "Lecture", related_name="ActiveLectures", on_delete=models.CASCADE)
    user = models.ForeignKey(
        "users.User", related_name="ActiveLectures", on_delete=models.CASCADE)
    progress = models.FloatField()
