from django import forms
from tkadventure.models import *


class BookingForm(forms.ModelForm):
    class Meta(object):
        model = Bookings
        fields = ('full_name','email','tour_name','quantity','message')
        widget = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'tour_name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'})

        }

class TourForm(forms.ModelForm):
    class Meta(object):
        model = Bookings
        fields = ('full_name','email','tour_name','quantity','message')
        widget = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'tour_name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'})

        }



class ContactForm(forms.ModelForm):
    class Meta(object):
        model = Contact
        fields = ('__all__')
        widget = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'})

        }