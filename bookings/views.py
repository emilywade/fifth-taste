from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import Table, Booking
from .forms import BookingForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
import logging
from django.contrib.auth.decorators import login_required


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

@login_required
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
                    user=request.user if request.user.is_authenticated else None,
                    table_number=table,
                    name=data['name'],
                    email=data['email'],
                    date=date,
                    time=time,
                    num_guests=num_guests,
                    special_requests=data['special_requests']
                )

                messages.success(
                    request, 'Your booking has been made successfully!')

                request.session['booking_name'] = data['name']
                request.session['booking_email'] = data['email']
                request.session['booking_date'] = str(data['date'])
                request.session['booking_time'] = str(data['time'])
                request.session['booking_num_guests'] = str(data['num_guests'])
                request.session['booking_special_requests'] = data['special_requests']
                request.session['booking_id'] = str(booking.booking_id)

                return redirect('booking_confirmation')

            else:
                messages.error(
                    request, 'No available tables for the selected time and date.')

                return render(request,
                              'bookings/create_booking.html',
                              {'form': form})

        else:
            return render(request,
                          'bookings/create_booking.html',
                          {'form': form})

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

@login_required
def manage_booking(request, booking_id):
    booking = get_object_or_404(Booking, booking_id=booking_id)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            updated_booking = form.save()

            messages.success(
                request, 'Your booking has been updated successfully.')

            return redirect(
                'booking_updated_confirmation',
                booking_id=updated_booking.booking_id)
    else:
        form = BookingForm(instance=booking)

    return render(request, 'bookings/manage_booking.html',
                  {'form': form, 'booking': booking})


logger = logging.getLogger(__name__)

@login_required
def delete_booking(request, booking_id):
    logger.debug(f"Attempting to delete booking with ID: {booking_id}")
    try:
        booking = get_object_or_404(Booking, booking_id=booking_id)
        logger.debug(f"Booking found: {booking}")
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        messages.error(request, f"Error: {str(e)}")
        return redirect('manage_booking', booking_id=booking_id)

    if request.method == 'POST':
        booking_data = {
            'name': booking.name,
            'email': booking.email,
            'date': booking.date.strftime('%Y-%m-%d'),
            'time': booking.time.strftime('%H:%M'),
            'num_guests': booking.num_guests,
            'special_requests': booking.special_requests,
            'booking_id': str(booking.booking_id),
        }

        request.session['deleted_booking'] = booking_data

        booking.delete()

        messages.success(
            request,
            "Your booking has been deleted successfully.")
        logger.debug(f"Redirecting to booking_cancellation")
        return redirect('booking_cancellation')

    return redirect('manage_booking', booking_id=booking_id)

@login_required
def booking_updated_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, booking_id=booking_id)

    return render(request,
                  'bookings/booking_updated_confirmation.html',
                  {'booking': booking})

@login_required
def booking_cancellation(request):
    booking_info = {
        'name': request.session.get('booking_name'),
        'email': request.session.get('booking_email'),
        'date': request.session.get('booking_date'),
        'time': request.session.get('booking_time'),
        'num_guests': request.session.get('booking_num_guests'),
        'special_requests': request.session.get('booking_special_requests'),
        'booking_id': request.session.get('booking_id'),
    }

    return render(request,
                  'bookings/booking_cancellation.html',
                  {'booking_info': booking_info})


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-date', '-time')
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})