from django.shortcuts import render, redirect
from .forms import ContactForm, EventQuoteForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required




class Home(FormView):
    template_name = 'ems/index.html'  
    form_class = ContactForm  # Ensure this is the correct form
    success_url = reverse_lazy('EMS_app:index')  # Redirect after successful submission

    def form_valid(self, form):
        contact_us_instance = form.save()  # Save the form if there are no errors

        # Prepare email details for the user
        user_subject = 'Thank you for contacting us!'
        user_message = (
            f"Hi {contact_us_instance.name},\n\n"
            f"Thank you for reaching out! We have received your message:\n\n"
            f"Name: {contact_us_instance.name}\n"
            f"Email: {contact_us_instance.email}\n"
            f"Phone Number: {contact_us_instance.number}\n"
            f"Message: {contact_us_instance.message}\n\n"
            "We will get back to you shortly."
        )
        from_email = settings.DEFAULT_FROM_EMAIL  # Set this in your settings
        user_recipient_list = [contact_us_instance.email]

        # Send email to the user
        try:
            send_mail(user_subject, user_message, from_email, user_recipient_list)
        except Exception as e:
            print(f"Error sending email to user: {e}")

        # Prepare email details for the admin
        admin_subject = 'New Contact Us Form Submission'
        admin_message = (
            f"New contact submission:\n\n"
            f"Name: {contact_us_instance.name}\n"
            f"Email: {contact_us_instance.email}\n"
            f"Phone Number: {contact_us_instance.number}\n"
            f"Message: {contact_us_instance.message}\n"
        )
        admin_recipient_list = ['saibhogadi999@gmail.com']  # Replace with your admin email

        # Send email to the admin
        try:
            send_mail(admin_subject, admin_message, from_email, admin_recipient_list)
        except Exception as e:
            print(f"Error sending email to admin: {e}")

        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)  # Log validation errors to the console
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()  # Get the form to pass to the template
        return context







class Quote(FormView):
    template_name = 'ems/quote.html'  # The template to render the form
    form_class = EventQuoteForm  # The form class to use
    success_url = reverse_lazy('EMS_app:index')  # Redirect after successful submission

    def form_valid(self, form):
        # Save the form data to the database
        event_quote_instance = form.save()  # Save the form if there are no errors

        # Prepare email details for the user
        user_subject = 'Thank you for your event quote request!'
        user_message = (
            f"Hi {event_quote_instance.name},\n\n"
            f"Thank you for reaching out! We have received your event quote request:\n\n"
            f"Event Type: {event_quote_instance.event_type}\n"
            f"Date and Time: {event_quote_instance.date_time}\n"
            f"Location: {event_quote_instance.location}\n"
            f"Number of Guests: {event_quote_instance.guests}\n"
            f"Budget: {event_quote_instance.budget}\n"
            f"Services: {event_quote_instance.services}\n"
            f"Special Requests: {event_quote_instance.requests}\n\n"
            "We will review your request and get back to you shortly."
        )
        from_email = settings.DEFAULT_FROM_EMAIL  # Use the default from email set in settings
        user_recipient_list = [event_quote_instance.email]  # Send the email to the user

        # Send email to the user
        try:
            send_mail(user_subject, user_message, from_email, user_recipient_list)
        except Exception as e:
            print(f"Error sending email to user: {e}")

        # Prepare email details for the admin
        admin_subject = 'New Event Quote Request'
        admin_message = (
            f"New event quote request:\n\n"
            f"Event Type: {event_quote_instance.event_type}\n"
            f"Date and Time: {event_quote_instance.date_time}\n"
            f"Location: {event_quote_instance.location}\n"
            f"Number of Guests: {event_quote_instance.guests}\n"
            f"Budget: {event_quote_instance.budget}\n"
            f"Services: {event_quote_instance.services}\n"
            f"Special Requests: {event_quote_instance.requests}\n"
            f"Name: {event_quote_instance.name}\n"
            f"Email: {event_quote_instance.email}\n"
            f"Phone Number: {event_quote_instance.number}\n"
        )
        admin_recipient_list = ['saibhogadi999@gmail.com']  # Replace with your admin email

        # Send email to the admin
        try:
            send_mail(admin_subject, admin_message, from_email, admin_recipient_list)
        except Exception as e:
            print(f"Error sending email to admin: {e}")

        return super().form_valid(form)  # Redirect to success_url after successful form submission

    def form_invalid(self, form):
        print(form.errors)  # Log validation errors to the console
        return super().form_invalid(form)  # Return the form with errors

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()  # Pass the form to the template context
        return context


 

def check_redirect(request):
    if request.user.is_authenticated:
        # Redirect to the named URL for the quote page (using app name and view name)
        return redirect('EMS_app:quote')  # Redirect to the quote page
    else:
        # Redirect to the login page (using app name and view name)
        return redirect('accounts:login')  # Redirect to the login page