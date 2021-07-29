from django.db import models
from core import models as core_models


class Writing(core_models.TimeStampedModel):
    user = models.ForeignKey(
        "users.User", related_name="writings", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
