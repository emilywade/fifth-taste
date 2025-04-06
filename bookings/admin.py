from django.contrib import admin
from .models import Table, Booking


class BookingAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email', 'date', 'time']

    list_filter = ['date', 'time', 'num_guests']

    list_display = ['name', 'table_number', 'date', 'time', 'num_guests', 'special_requests']

    list_editable = ['num_guests', 'special_requests']

    fields = ['name', 'email', 'date', 'time', 'num_guests', 'special_requests']


# Register your models here.
admin.site.register(Table)
admin.site.register(Booking, BookingAdmin)