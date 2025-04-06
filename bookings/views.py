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
            data = form.cleaned_data
            date = data['date']
            time = data['time']
            num_guests = data['num_guests']
            
            available_tables = get_available_tables(date, time, num_guests)
            
            # print("Available tables:", available_tables)
            
            if available_tables:
            
                table = available_tables[0]
                # print(table)
                
                Booking.objects.create(
                    table_number=table,
                    name=data['name'],
                    email=data['email'],
                    date=date,
                    time=time,
                    num_guests=num_guests,
                    special_requests=data['special_requests']
                ) 
                
                
            else:
                print('no table available')
        
        else:
            print("form invalid")
            
    else:
        form = BookingForm()
    return render(request, 'bookings/create_booking.html', {'form': form})



def home(request):
    return render(request, 'bookings/home.html')
