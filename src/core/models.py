# django
from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    """Model definition for Model."""

    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        abstract = True
