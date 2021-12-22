from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# hi

class User(AbstractUser):

    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )
    PERSON_TEACHER = "teacher"
    PERSON_STUDENT = "student"

    PERSON_CHOICES = (
        (PERSON_TEACHER, "Teacher"),
        (PERSON_STUDENT, "Student"),
    )

    avatar = models.ImageField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthday = models.DateField(blank=True, null=True)
    teacher = models.CharField(choices=PERSON_CHOICES, max_length=10)
