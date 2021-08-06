from django.db import models
from main.models import Patient, Package

import uuid
import datetime

from commonfunctions import GetTimeString, GetDateString

class Day(models.Model):
	Date = models.DateField(default=datetime.datetime.now().date(), primary_key=True)

	def __str__(self):
		return self.Date.__str__()

class Slot(models.Model):
	Patient = models.ForeignKey(Patient, null=True, blank=True, on_delete=models.CASCADE, related_name="Patient")
	DateAlloted = models.ForeignKey(Day, on_delete=models.CASCADE, related_name="DateAlloted")
	TimeAlloted = models.TimeField(default=datetime.datetime.now().time())
	Description = models.TextField(null=True, blank=True)
	Package = models.ForeignKey(Package, null=True, blank=True, on_delete=models.CASCADE, related_name="Package")

	def __str__(self):
		date = datetime.datetime.combine(self.DateAlloted.Date, self.TimeAlloted)
		if self.Patient is not None:
			return self.Patient.User.username + ' on ' + date.__str__()
		else:
			return date.__str__()

	def GetSlotValue(self):
		return f'{GetDateString(self.DateAlloted.Date)} : {GetTimeString(datetime.datetime.combine(self.DateAlloted.Date, self.TimeAlloted))}'

	def GetSlotDescription(self):
		time = datetime.datetime.combine(self.DateAlloted.Date, self.TimeAlloted)
		till = time + datetime.timedelta(hours=1)
		return f'{GetTimeString(time)} to {GetTimeString(till)}'