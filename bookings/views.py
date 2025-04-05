from django.shortcuts import render
from .models import Table

# Create your views here.
def table_list(request):
    tables = Table.objects.all()
    
    return render(request, 'bookings/table_list.html', {'tables': tables})
