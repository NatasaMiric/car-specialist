from django.contrib import admin
from django.db import models
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer', 'service_type', 'created_on')
    search_fields = ['customer']
    list_filter = ('created_on',)
    actions = ['approve_bookings']

    def approve_bookings(self, request, queryset):
        queryset.update(approved=True)