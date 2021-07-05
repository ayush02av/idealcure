from django.db import models
from django.contrib.auth.models import User

import uuid
import datetime

class Patient(models.Model):
	User = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	Age = models.IntegerField(null=True, blank=True)
	Address = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.User.get_full_name() + ' - ' + self.User.username

class PatientRecord(models.Model):
	Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	Date = models.DateTimeField(default=datetime.datetime.now())
	Report = models.TextField()

	def __str__(self):
		return self.Patient.__str__() + ' on ' + self.Date.__str__()

class PatientFile(models.Model):
	Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	Title = models.CharField(max_length=50,null=True, blank=True)
	Date = models.DateTimeField(default=datetime.datetime.now())
	File = models.FileField(upload_to ='patientfiles/')

	def __str__(self):
		return self.Patient.__str__() + ' - ' + self.Title + ' on ' + self.Date.date().__str__()

class Treatment(models.Model):
	Name = models.CharField(max_length=50, primary_key=True)
	Description = models.TextField()
	ImageLink = models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		return self.Name

class FAQ(models.Model):
	Question = models.TextField()
	Answer = models.TextField()

	def __str__(self):
		return self.Question