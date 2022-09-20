from django.contrib import admin

from .models import Slot, Appointment


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    '''Admin View for slot'''


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    '''Admin View for Appointment'''
