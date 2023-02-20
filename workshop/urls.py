from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('booking/', views.BookingView.as_view(), name='booking'),
    path('services/', views.ServicesPage.as_view(), name='services'),
]
