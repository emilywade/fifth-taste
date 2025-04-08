from django.test import TestCase
from .forms import BookingForm
from .models import Booking
from django.core.exceptions import ValidationError

class BookingFormTest(TestCase):

    def test_form_valid_data(self):
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'num_guests': 2,
            'special_requests': 'No nuts',
            'date': '2025-04-10',
            'time': '18:00',
        }
        form = BookingForm(data=data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        data = {
            'name': '',
            'email': '',
            'num_guests': '',
            'special_requests': 'No nuts',
            'date': '2025-04-10',
            'time': '18:00',
        }
        form = BookingForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertIn('email', form.errors)

    def test_email_field_invalid_format(self):
        data = {
            'name': 'John Doe',
            'email': 'invalidemail',
            'num_guests': 2,
            'special_requests': 'No nuts',
            'date': '2025-04-10',
            'time': '18:00',
        }
        form = BookingForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_clean_num_guests(self):
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'num_guests': -2,
            'special_requests': 'No nuts',
            'date': '2025-04-10',
            'time': '18:00',
        }
        form = BookingForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('num_guests', form.errors)
