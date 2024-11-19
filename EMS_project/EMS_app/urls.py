from django.urls import path
from .views import Home, Quote, check_redirect

app_name = 'EMS_app'

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('quote/', Quote.as_view(), name='quote'),
    path('submit/', Quote.as_view(), name='submit'),
    path('check-redirect/', check_redirect, name='check_redirect'),
]
