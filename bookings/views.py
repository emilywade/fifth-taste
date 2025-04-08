from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import Table, Booking
from .forms import BookingForm, LookupBookingForm
from django.contrib import messages
from django.shortcuts import get_object_or_404


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
            data = form.cleaned_data
            date = data['date']
            time = data['time']
            num_guests = data['num_guests']
            
            available_tables = get_available_tables(date, time, num_guests)
                        
            if available_tables:
            
                table = available_tables[0]
                
                booking = Booking.objects.create(
                    table_number=table,
                    name=data['name'],
                    email=data['email'],
                    date=date,
                    time=time,
                    num_guests=num_guests,
                    special_requests=data['special_requests']
                )
                
                messages.success(request, 'Your booking has been made successfully!')
                
                request.session['booking_name'] = data['name']
                request.session['booking_email'] = data['email']
                request.session['booking_date'] = str(data['date'])
                request.session['booking_time'] = str(data['time'])
                request.session['booking_num_guests'] = str(data['num_guests'])
                request.session['booking_special_requests'] = data['special_requests']
                request.session['booking_id'] = str(booking.booking_id)
                
                return redirect('booking_confirmation')
                
            else:
                messages.error(request, 'No available tables for the selected time and date.')
                
                return render(request, 'bookings/create_booking.html', {'form': form})
        
        else:
            return render(request, 'bookings/create_booking.html', {'form': form})
            
    else:
        form = BookingForm()
        return render(request, 'bookings/create_booking.html', {'form': form})



def home(request):
    return render(request, 'home.html')


def menu(request):
    return render(request, 'menu.html')


def booking_confirmation(request):
    context = {
        'booking_name': request.session.get('booking_name'),
        'booking_email': request.session.get('booking_email'),
        'booking_date': request.session.get('booking_date'),
        'booking_time': request.session.get('booking_time'),
    }
    return render(request, 'bookings/booking_confirmation.html', context)
