from django.db import models
from django.contrib.auth import get_user_model

from core.models import BaseModel

User = get_user_model()


class Slot(BaseModel):
    """Model definition for Slot."""

    name = models.CharField(max_length=50, default='name')
    start = models.DateTimeField()
    end = models.DateTimeField()

    class Meta:
        """Meta definition for Slot."""

        verbose_name = 'Slot'
        verbose_name_plural = 'Slots'

    def __str__(self):
        """Unicode representation of Slot."""
        return f'{self.name} <{self.start} - {self.end}>'


class Appointment(BaseModel):
    """Model definition for Appointment."""

    slot = models.ForeignKey(
        'Slot',
        on_delete=models.CASCADE,
        related_name='appointment',
    )

    patient = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='bookings',
    )
    doctor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='appointments',
    )

    class Meta:
        """Meta definition for Appointment."""

        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'

    def __str__(self):
        """Unicode representation of Appointment."""

        return f"{self.patient} {self.slot}"
