from main.models import Treatment, Package
from django.contrib.auth.models import User
import datetime

def Treatments():
	return Treatment.objects.all()

def Packages():
	return Package.objects.all()

time_string_format = '%I:%M %p'

def GetTimeString(datetime_instance):
	return datetime_instance.strftime(time_string_format)

def GetDateString(datetime_instance):
	return datetime_instance.strftime('%a, %d of %b, %Y')