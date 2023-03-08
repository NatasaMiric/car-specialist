from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import (CreateView, UpdateView, DeleteView, FormView,
                                  TemplateView)
from .models import Booking
from .forms import BookingForm, ContactForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePage(View):

    def get(self, request):
        return render(request, 'index.html')


class BookingView(LoginRequiredMixin, CreateView):
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


class MyBookingsPage(LoginRequiredMixin, View):

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


class UpdateBooking(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'edit_booking.html'
    success_url = reverse_lazy('mybookings')
    success_message = "Your booking was updated successfully"


class DeleteBooking(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = 'delete_booking.html'
    success_url = reverse_lazy('home')
    success_message = "Your booking was deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteBooking, self).delete(request, *args, **kwargs)


class ServicesPage(View):

    def get(self, request):
        return render(request, 'services.html')


class ContactPage(FormView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        self.send_mail(form.cleaned_data)
        return super(ContactPage, self).form_valid(form)

    def send_mail(self, valid_data):
        # send mail logic
        print(valid_data)
        pass


class SuccessView(TemplateView):
    template_name = 'success.html'
