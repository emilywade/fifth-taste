from django.urls import path
from . import views

urlpatterns = [
    # path('tables/', views.table_list, name='table_list'),
    path('bookings/', views.create_booking, name='create_booking'),
]