from django.urls import path
from . import views

urlpatterns = [
    path('bookings/', views.create_booking, name='create_booking'),
    path('booking-confirmation/', views.booking_confirmation, name='booking_confirmation'),
    path('', views.home, name='home'), 
]