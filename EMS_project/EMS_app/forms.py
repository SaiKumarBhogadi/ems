from django import forms
from .models import Contact, EventQuote

class EventQuoteForm(forms.ModelForm):
    class Meta:
        model = EventQuote
        fields = [
            'event_type', 
            'date_time', 
            'location', 
            'guests', 
            'budget', 
            'services', 
            'requests', 
            'name', 
            'email', 
            'number'
            
        ]
        
        widgets = {
            'event_type': forms.Select(attrs={
                'class': 'form-select',
                'required': True
            }),
            'date_time': forms.DateTimeInput(attrs={
                'class': 'form-input', 
                'placeholder': 'Select date and time', 
                'required': True,
                'type': 'datetime-local'  # Specify datetime-local input type
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-input', 
                'placeholder': 'Enter event location', 
                'required': True
            }),
            'guests': forms.NumberInput(attrs={
                'class': 'form-input', 
                'placeholder': 'Number of guests', 
                'required': True
            }),
            'budget': forms.NumberInput(attrs={
                'class': 'form-input', 
                'placeholder': 'Enter your budget', 
                'required': True
            }),
            'services': forms.Select(attrs={
                'class': 'form-select', 
                'required': True
            }),
            'requests': forms.Textarea(attrs={
                'class': 'form-textarea', 
                'placeholder': 'Any special requests...', 
                'required': False
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-input', 
                'placeholder': 'Enter your name', 
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input', 
                'placeholder': 'Enter your email', 
                'required': True
            }),
            'number': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter your phone number ',
                'required': True,
                
            }),
        }




class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'number', 'message']
        
        widgets = {
            'name': forms.TextInput(attrs={ 
                'class': 'form-input', 
                'placeholder': 'Enter your name', 
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input', 
                'placeholder': 'Enter your email', 
                'required': True
            }),
            'number': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter your phone number ',
                'required': True,
               
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-textarea', 
                'placeholder': 'Write your message here...', 
                'required': True
            }),
        }
