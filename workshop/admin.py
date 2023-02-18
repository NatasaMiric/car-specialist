from django.contrib import admin
from django.db import models
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'service_type', 'created_on', 'approved')
    search_fields = ['user']
    list_filter = ('created_on', 'approved')
    actions = ['approve_bookings']

    def approve_bookings(self, request, queryset):
        queryset.update(approved=True)
