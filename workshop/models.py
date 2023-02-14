from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

SERVICE_TYPE = (
    ('Vehicle Diagnostics', 'Vehicle Diagnostics'),
    ('Start and charging system repairs', 'Start and charging system repairs'),
    ('Replacement of light bulbs', 'Replacement of light bulbs'),
    ('Clutch replacement', 'Clutch replacement'),
    ('Cambelt repair', 'Cambelt repair'),
    ('Basic service', 'Basic service'),
    ('Big service', 'Big service'),
    ('Electronic systems repair', 'Electronic systems repair'),
    ('Tire change and repair', 'Tire change and repair')
)

AVAILABLE_TIME = (
    ('8:00am-9:00am', '8:00am-9:00am'),
    ('9:00am-10:00am', '9:00am-10:00am'),
    ('10:00am-11:00am', '10:00am-11:00am'),
    ('12:00am-13:00pm', '12:00am-13:00pm'),
    ('13:00pm-14:00pm', '13:00pm-14:00pm'),
    ('14:00pm-15:00pm', '14:00pm-15:00pm'),
)


class Booking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name="user_bookings")
    phone_number = models.CharField(max_length=12)
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPE, 
                                    default='')
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=15, choices=AVAILABLE_TIME, 
                            default='8:00am-9:00am')
    comment = models.TextField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.customer} | service: {self.service_type} | day: {self.day} | time: {self.time}"
