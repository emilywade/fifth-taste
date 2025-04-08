from django import forms
from .models import Booking
import datetime


class BookingForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Email Address')
    time = forms.ChoiceField(label='Time')

    class Meta:
        model = Booking
        fields = [
            'name',
            'email',
            'date',
            'time',
            'num_guests',
            'special_requests']
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date'}), 'special_requests': forms.TextInput(
                attrs={
                    'rows': 3, 'placeholder': 'Any special requests?'}), }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Generate 30-min slot choices between 12–15:30 and 17–21:30
        opening_hours = [(12, 16), (17, 22)]
        slots = []
        for start, end in opening_hours:
            current = datetime.time(hour=start)
            while current < datetime.time(hour=end):
                slots.append(
                    (current.strftime("%H:%M"),
                     current.strftime("%H:%M")))
                # Add 30 minutes
                h, m = current.hour, current.minute
                if m == 0:
                    current = datetime.time(hour=h, minute=30)
                else:
                    current = datetime.time(hour=h + 1, minute=0)

        self.fields['time'].choices = slots
