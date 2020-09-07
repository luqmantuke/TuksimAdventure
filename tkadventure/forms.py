from django import forms
from tkadventure.models import Bookings


class BookingForm(forms.ModelForm):
    class Meta(object):
        model = Bookings
        fields = ('__all__')
        widget = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'tour_name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'})

        }
    