# django
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserKind(models.IntegerChoices):
    ADMIN = 1
    DOCTOR = 2
    CUSTOMER = 3


class User(AbstractUser):
    """Model definition for User."""

    kind = models.PositiveSmallIntegerField(
        choices=UserKind.choices,
        default=UserKind.CUSTOMER,
    )
