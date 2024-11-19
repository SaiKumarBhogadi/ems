from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from .forms import RegistrationForm




def accounts(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = RegistrationForm()
    return render(request, "accounts/register.html", { "form" : form })

@login_required
def admin_dashboard(request):
    return render(request, 'accounts/admin_dashboard.html', {})

 
