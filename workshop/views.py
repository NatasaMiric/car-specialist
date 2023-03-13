from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import (CreateView, UpdateView, DeleteView, FormView,
                                  TemplateView)
from .models import Booking
from .forms import BookingForm, ContactForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePage(View):
    """
    View to render homepage.
    """
    def get(self, request):
        return render(request, 'index.html')


class BookingView(LoginRequiredMixin, CreateView):
    """
    View to render the page where user creates a booking.
    """
    form_class = BookingForm
    template_name = 'booking.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            if (check_duplicate_booking(request.user, request.POST['day'],
                                        request.POST['time'],)):
                form.add_error(
                                None,
                                'Selected time is not available.'
                                ' Please choose another time')
                return render(request, self.template_name, {'form': form})
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('mybookings')
        return render(request, self.template_name, {'form': form})


def check_duplicate_booking(user, day, time, pk=None):
    """
    Function to prevent same time bookings
    """
    if pk:
        bookings = Booking.objects.filter(user=user, day=day,
                                          time=time).exclude(id=pk)
    else:
        bookings = Booking.objects.filter(day=day, time=time)
    if len(bookings):
        return True


class MyBookingsPage(LoginRequiredMixin, View):
    """
    View to render bookings that customer submited and it's data.
    """

    def get(self, request):
        user = request.user
        if request.user.is_authenticated:
            bookings = (Booking.objects.filter(user=self.request.user).
                        order_by('-created_on'))
            context = {
                    'user': user,
                    'bookings': bookings,
            }
            return render(request, 'mybookings.html', context)
        else:
            return render(request, 'account/login.html')


class UpdateBooking(LoginRequiredMixin, UpdateView):
    """
    View to render update booking page.
    """
    model = Booking
    form_class = BookingForm
    template_name = 'update_booking.html'
    success_url = reverse_lazy('mybookings')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.get_object())
        if form.is_valid():
            if (check_duplicate_booking(request.user, request.POST['day'],
                                        request.POST['time'],
                                        pk=self.request.GET.get('pk')
                                        )):
                form.add_error(
                                None,
                                'Selected time is not available.'
                                ' Please choose another time')
                return render(request, self.template_name, {'form': form})
            booking = form.save()
            booking.approved = False
            booking.save()
            messages.success(request, 'Booking updated successfully')
            return redirect('mybookings')
        return render(request, self.template_name, {'form': form})

    def get_object(self, queryset=None):
        return get_object_or_404(Booking, pk=self.kwargs.get("pk"),
                                 user=self.request.user)


class DeleteBooking(LoginRequiredMixin, DeleteView):
    """
    View to render delete page.
    """
    model = Booking
    template_name = 'delete_booking.html'
    success_url = reverse_lazy('mybookings')
    success_message = "Your booking was deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteBooking, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return get_object_or_404(Booking, pk=self.kwargs.get("pk"),
                                 user=self.request.user)


class ServicesPage(View):
    """
    View to render services page.
    """
    def get(self, request):
        return render(request, 'services.html')


class ContactPage(FormView):
    """
    View to render contact page.
    """
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        return super(ContactPage, self).form_valid(form)


class SuccessView(TemplateView):
    """
    View to render success page.
    """
    template_name = 'success.html'


def handler404(request, exception):
    """
    Creates custom 404 error page
    """
    context = {}
    response = render(request, "404.html", context=context)
    response.status_code = 404
    return response
