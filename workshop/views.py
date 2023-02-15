from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from .models import Booking
from .forms import BookingForm


class HomePage(View):

    def get(self, request):
        return render(request, 'index.html')


class BookingView(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking.html'
    success_url = 'booking'
