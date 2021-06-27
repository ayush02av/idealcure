from django.db import models
from main.models import Patient

import uuid
import datetime

class Day(models.Model):
	Date = models.DateField(default=datetime.datetime.now().date(), primary_key=True)

	def __str__(self):
		return self.Date.__str__()

class Slot(models.Model):
	Patient = models.ForeignKey(Patient, null=True, blank=True, on_delete=models.CASCADE)
	DateAlloted = models.ForeignKey(Day, on_delete=models.CASCADE)
	TimeAlloted = models.TimeField(default=datetime.datetime.now().time())
	Description = models.TextField(null=True, blank=True)

	def __str__(self):
		date = datetime.datetime.combine(self.DateAlloted.Date, self.TimeAlloted)
		if self.Patient is not None:
			return self.Patient.User.username + ' on ' + date.__str__()
		else:
			return date.__str__()