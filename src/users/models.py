# django
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class UserKind(models.IntegerChoices):
    ADMIN = 1
    DOCTOR = 2
    PATIENT = 3


class User(AbstractUser):
    """Model definition for User."""

    kind = models.PositiveSmallIntegerField(
        choices=UserKind.choices,
        default=UserKind.PATIENT,
    )

    objects: UserManager


class PatientProfile(models.Model):
    """ just for testing nested create and nested query"""

    user = models.OneToOneField('User', on_delete=models.CASCADE)
    address = models.TextField()
