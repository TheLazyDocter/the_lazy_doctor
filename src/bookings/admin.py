# django
from django.contrib import admin

# local
from .models import Appointment, Slot


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    '''Admin View for slot'''


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    '''Admin View for Appointment'''
