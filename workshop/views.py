from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import CreateView
from .models import Booking
from .forms import BookingForm
from django.http import HttpResponseRedirect


class HomePage(View):

    def get(self, request):
        return render(request, 'index.html')


class BookingView(CreateView):
    form_class = BookingForm    
    template_name = 'booking.html'
    context = {}
   
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():       
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('home')
        else:
            print(form.errors)

        return render(request, self.template_name, {'form': form})