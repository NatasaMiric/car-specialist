from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('customer', 'phone_number', 'service_type', 'day', 'time',
                  'comment')

        widgets = {
            'customer': forms.TextInput(attrs={'class': 'form-control',
                                        'placeholder': 'Full Name',
                                               'style': 'width: 300px;'
                                               }),
            'phone_number': forms.TextInput(attrs={'class': 'form-control',
                                                   'style': 'width: 300px;'
                                                   }),
            'service_type': forms.Select(),
            'day':  forms.NumberInput(attrs={'type': 'date'}),
            'time': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control',
                                      'placeholder': 'Describe your case here'}
                                      )
        }
