# builtins
from datetime import datetime

# third party
import strawberry

from strawberry import auto, django

# local
from ..models import Appointment, Slot


@django.input(Slot)
class SlotInput:
    start: datetime
    end: datetime


@django.input(Appointment)
class AppointmentInput:
    slot: SlotInput


# ==============================================
# ==============================================


@django.type(Slot)
class SlotType:
    id: auto
    start: datetime
    end: datetime


@django.type(Appointment)
class AppointmentType:
    id: strawberry.ID
    # slot: SlotType


@strawberry.type
class BookingMutation:

    @strawberry.mutation
    def make_a_booking(self, input: AppointmentInput) -> AppointmentType:
        print(f'Adding {self}')

        return AppointmentType(id="khaskdhkasd")
