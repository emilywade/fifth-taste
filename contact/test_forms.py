from django.test import TestCase
from .forms import ContactForm

class ContactFormTest(TestCase):

    def test_contact_form_valid_data(self):
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'message': 'This is a test message',
        }
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid())

    def test_contact_form_invalid_data(self):
        data = {
            'name': '',
            'email': '',
            'message': '',
        }
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('message', form.errors)

    def test_contact_form_invalid_email(self):
        data = {
            'name': 'John Doe',
            'email': 'invalidemail',
            'message': 'This is a test message',
        }
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_contact_form_success(self):
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'message': 'This is a test message',
        }
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid())
