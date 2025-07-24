from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
import uuid


class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"Table {self.table_number} (Seats {self.capacity})"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    booking_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True)
    table_number = models.ForeignKey(
        'Table',
        on_delete=models.SET_NULL,
        null=True,
        blank=True)

    name = models.CharField(max_length=100)
    email = models.EmailField()

    date = models.DateField()
    time = models.TimeField()
    num_guests = models.PositiveIntegerField()
    special_requests = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    duration = timedelta(hours=2)

    def __str__(self):
        return f"Booking {
            self.booking_id} for {
            self.name} on {
            self.date} at {
                self.time} ({
                    self.num_guests} guests)"
