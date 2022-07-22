from cgitb import reset
import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Companies

# Create your tests here.
def create_companies(companies_name, days):
    time= timezone.now() + datetime.timedelta(days=days)
    return Companies.objects.create(companies_name= companies_name, pub_date= time)