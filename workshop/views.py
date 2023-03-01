from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Booking
from .forms import BookingForm
from django.urls import reverse_lazy


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
        if request.user.is_authenticated:
            bookings = (Booking.objects.filter(user=self.request.user).
                        order_by('day', 'time'))
            context = {
                    'user': user,
                    'bookings': bookings,
            }
            return render(request, 'mybookings.html', context)
        else:
            return render(request, 'account/login.html')


class UpdateBooking(UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'edit_booking.html'


class DeleteBooking(DeleteView):
    model = Booking
    template_name = 'delete_booking.html'
    success_url = reverse_lazy('home')


class ServicesPage(View):

    def get(self, request):
        return render(request, 'services.html')
