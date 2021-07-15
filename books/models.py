from django.db import models
from core import models as core_models

# Create your models here.


class Book(core_models.TimeStampedModel):
    title = models.CharField(max_length=10)
    bookcover = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=10)
    author = models.CharField(max_length=10)
