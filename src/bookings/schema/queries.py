import strawberry

from datetime import datetime

from ..models import Slot, Appointment


@strawberry.type
class SlotType:
    id: strawberry.ID
    start: datetime
    end: datetime


@strawberry.type
class AppointmentType:
    id: strawberry.ID
    slot: SlotType


def make_a_booking() -> list[AppointmentType]:
    return Appointment.objects.all()
