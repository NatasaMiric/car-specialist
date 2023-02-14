# Generated by Django 3.2.17 on 2023-02-14 17:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=12)),
                ('service_type', models.CharField(choices=[('Vehicle Diagnostics', 'Vehicle Diagnostics'), ('Start and charging system repairs', 'Start and charging system repairs'), ('Replacement of light bulbs', 'Replacement of light bulbs'), ('Clutch replacement', 'Clutch replacement'), ('Cambelt repair', 'Cambelt repair'), ('Basic service', 'Basic service'), ('Big service', 'Big service'), ('Electronic systems repair', 'Electronic systems repair'), ('Tire change and repair', 'Tire change and repair')], default='', max_length=50)),
                ('day', models.DateField(default=datetime.datetime.now)),
                ('time', models.CharField(choices=[('8:00am-9:00am', '8:00am-9:00am'), ('9:00am-10:00am', '9:00am-10:00am'), ('10:00am-11:00am', '10:00am-11:00am'), ('12:00am-13:00pm', '12:00am-13:00pm'), ('13:00pm-14:00pm', '13:00pm-14:00pm'), ('14:00pm-15:00pm', '14:00pm-15:00pm')], default='8:00am-9:00am', max_length=15)),
                ('comment', models.TextField(max_length=250)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_bookings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
