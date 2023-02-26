from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView
from .models import Booking
from .forms import BookingForm


class HomePage(View):

    def get(self, request):
        return render(request, 'index.html')


class BookingView(CreateView):
    form_class = BookingForm
    template_name = 'booking.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('mybookings')
        else:
            print(form.errors)

        return render(request, self.template_name, {'form': form})


class MyBookingsPage(View):

    def get(self, request):
        user = request.user
        bookings = Booking.objects.filter(user=user).order_by('day', 'time')
        context = {
            'user': user,
            'bookings': bookings,
        }
        return render(request, 'mybookings.html', context)


class UpdateBooking(UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'edit_booking.html'


class ServicesPage(View):

    def get(self, request):
        return render(request, 'services.html')
