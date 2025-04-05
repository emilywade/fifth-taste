from django.shortcuts import render
from django.views import generic
from .models import Table

# Create your views here.
class TableList(generic.ListView):
    queryset = Table.objects.all()
    template_name = "bookings/table_list.html"