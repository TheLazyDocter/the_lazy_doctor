import strawberry

# third party
import strawberry
from strawberry import django, auto
from datetime import datetime
# local
from .models import Appointment, Slot, User

@django.input(Slot)
class SlotInput:
    start: datetime
    end: datetime

@django.input(Appointment)
class AppointmentInput:
    slot: strawberry.ID

@django.type(Slot)
class SlotType:
    id: auto
    start: datetime
    end: datetime

@django.type(Appointment)
class AppointmentType:
    id: auto
    slot: SlotType
