from django.shortcuts import render
from datetime import datetime, timedelta
from .models import Table, Booking
from .forms import BookingForm


def get_available_tables(date, time, num_guests):
    
    booking_start = time
    time = datetime.strptime(time, "%H:%M").time()
    booking_end = (datetime.combine(date, time) + timedelta(hours=2)).time()

    candidate_tables = Table.objects.filter(capacity__gte=num_guests)

    booked_tables = Booking.objects.filter(
        date=date,
        time__lt=booking_end,
    ).filter(
        time__gte=booking_start
    ).values_list('table_number', flat=True)

    available_tables = candidate_tables.exclude(id__in=booked_tables)

    return available_tables


def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            num_guests = form.cleaned_data['num_guests']
            
            available_tables = get_available_tables(date, time, num_guests)
            
            
            print("Available tables:", available_tables)
            
    else:
        form = BookingForm()
    return render(request, 'bookings/create_booking.html', {'form': form})



def home(request):
    return render(request, 'bookings/home.html')
