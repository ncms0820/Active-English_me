from django.db import models
from core import models as core_models
# Create your models here.


class Post(core_models.TimeStampedModel):
    contents = models.TextField(max_length=255)
    user = models.ForeignKey("users.User", related_name="posts", on_delete=models.CASCADE)
    likes = models.ManyToManyField("users.User", blank=True, null=True)

    def total_likes(self):
        return self.likes.count()


class Comment(core_models.TimeStampedModel):
    post = models.ForeignKey("Post", related_name="comments", on_delete=models.CASCADE, null=True)
    contents = models.TextField(max_length=100)
    user = models.ForeignKey(
        "users.User", related_name="comments", on_delete=models.SET_NULL, null=True)
