from database import models
from django.contrib.auth.models import User
import datetime

def Treatments():
	return models.Treatment.objects.all()

def Packages():
	return models.Package.objects.all()

time_string_format = '%I:%M %p'

def GetTimeString(datetime_instance):
	return datetime_instance.strftime(time_string_format)

def GetDateString(datetime_instance):
	return datetime_instance.strftime('%a, %d of %b, %Y')

def GetSlots():
	slots = dict()
	for day in models.Day.objects.all():
		if (day.Date >= datetime.datetime.today().date()):
			slots[day] = models.Slot.objects.filter(DateAlloted=day, PatientTreatment=None)
	datelist = list(slots.keys())
	return (slots, datelist)