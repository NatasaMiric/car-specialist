from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('booking/', views.BookingView.as_view(), name='booking'),
    path('services/', views.ServicesPage.as_view(), name='services'),
    path('mybookings/', views.MyBookingsPage.as_view(), name='mybookings'),
    path('mybookings/update_booking/<int:pk>/', views.UpdateBooking.as_view(),
         name='update_booking'),
    path('mybookings/<int:pk>/delete_booking', views.DeleteBooking.as_view(),
         name='delete_booking'),
    path('contact/', views.ContactPage.as_view(), name='contact'),
    path("success/", views.SuccessView.as_view(), name="success")
]
