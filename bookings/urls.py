from django.urls import path
from . import views

urlpatterns = [
    path('bookings/', views.create_booking, name='create_booking'),
    path('booking-confirmation/', views.booking_confirmation, name='booking_confirmation'),
    path('menu/', views.menu, name='menu'),
    path('', views.home, name='home'), 
    path('manage_booking/<uuid:booking_id>/', views.manage_booking, name='manage_booking'),
]