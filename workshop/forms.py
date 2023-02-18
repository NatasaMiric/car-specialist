from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking

        fields = ('user', 'phone_number', 'service_type', 'day', 'time',
                  'comment')
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control',
                                    'style': 'width: 300px;'
                                    }),
            'phone_number': forms.TextInput(attrs={'class': 'form-control',
                                                   'style': 'width: 300px;'
                                                   }),
            'service_type': forms.Select(),
            'day':  forms.NumberInput(attrs={'type': 'date'}),
            'time': forms.Select(),
            'comment': forms.Textarea(attrs={'class': 'form-control',
                                      'placeholder': 'Describe your case here'}
                                      )
        }
        labels = {
            'user': 'Full Name'
        }