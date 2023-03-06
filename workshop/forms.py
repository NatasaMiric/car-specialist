from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking

        fields = ('phone_number', 'service_type', 'day', 'time', 'comment')
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control',
                                                   'style': 'max-width: 300px;'
                                                   }),
            'service_type': forms.Select(attrs={'class': 'form-control',
                                                'style': 'max-width:300px;'}),
            'day':  forms.NumberInput(attrs={'type': 'date'}),
            'time': forms.Select(),
            'comment': forms.Textarea(attrs={'class': 'form-control',
                                      'placeholder': 'Describe your case here'}
                                      )
        }


class ContactForm(forms.Form):

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'style': 'max-width: 300px;'}
    ), max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'style': 'max-width: 300px;'}
    ), max_length=50)
    email_address = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'style': 'max-width: 300px;'}
    ), max_length=50)
    message = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'style': 'max-width: 300px;'}
    ), max_length=1000)
