from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core.validators import RegexValidator
import phonenumbers

# Validator for phone number using RegexValidator
phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
)

class NumberValidation(models.Model):
    phone_number = models.CharField(validators=[phone_regex], max_length=17)

    def clean(self):
        super().clean()
        try:
            input_number = phonenumbers.parse(self.phone_number)
            if not phonenumbers.is_valid_number(input_number):
                raise ValidationError("Invalid phone number.")
        except phonenumbers.phonenumberutil.NumberParseException:
            raise ValidationError("Invalid phone number.")

# EventQuote model with phone number validation
class EventQuote(models.Model):
    event_type = models.CharField(max_length=50, choices=[
        ('wedding', 'Wedding'),
        ('birthday', 'Birthday'),
        ('party', 'Party'),
        ('corporate', 'Corporate')
    ])
    date_time = models.DateTimeField()
    location = models.CharField(max_length=300)
    guests = models.IntegerField()
    budget = models.IntegerField()
    services = models.CharField(max_length=50, choices=[
        ('Catering', 'Catering'),
        ('Decoration', 'Decoration'),
        ('Entertainment', 'Entertainment'),
        ('Photography', 'Photography'),
        ('Venue', 'Venue'),
        ('All', 'All')
    ])
    requests = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(validators=[phone_regex], max_length=17)  # Updated for phone validation

    def __str__(self):
        return f"{self.name} - {self.event_type} - {self.budget}"

# Contact model with phone number validation
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(validators=[phone_regex], max_length=17)  # Updated for phone validation
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
