from django.db import models
from commonfunctions import GetTimeString, GetDateString
from django.contrib.auth.models import AbstractUser

import uuid, datetime
from django.utils import timezone

def datetime_now():
	return timezone.now()

def datetime_date():
	return timezone.now().date()

def datetime_time():
	return timezone.now().time()

class Treatment(models.Model):
	Name = models.CharField(max_length=50, primary_key=True)
	Description = models.TextField()
	ImageLink = models.CharField(max_length=50, null=True, blank=True)

class User(AbstractUser):
	Address = models.TextField(null=True, blank=True)
	Age = models.IntegerField(null=True, blank=True)
	Gender = models.CharField(max_length=6, null=True, blank=True)
	password = models.CharField(max_length=100, editable=False)

class Patient(models.Model):
	User = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	PatientVerified = models.BooleanField(default=False)

class PatientTreatment(models.Model):
	Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	Treatment = models.ForeignKey(Treatment, null=True, blank=True, on_delete=models.CASCADE, related_name="Treatment")
	Date = models.DateField(default=datetime_date)
	Validity = models.CharField(max_length=10)
	ClosedStatus = models.BooleanField(default=False)

class PatientRecord(models.Model):
	PatientTreatment = models.ForeignKey(PatientTreatment, on_delete=models.CASCADE)
	Date = models.DateTimeField(default=datetime_now)
	Report = models.TextField()

class PatientFile(models.Model):
	PatientTreatment = models.ForeignKey(PatientTreatment, on_delete=models.CASCADE)
	Title = models.CharField(max_length=50,null=True, blank=True)
	Date = models.DateTimeField(default=datetime_now)
	File = models.FileField(upload_to ='patientfiles/')

class FAQ(models.Model):
	Question = models.TextField()
	Answer = models.TextField()

class Package(models.Model):
	Price = models.IntegerField(primary_key=True)
	Duration = models.CharField(max_length=10)
	Description = models.TextField(max_length=100)
	PaymentLink = models.CharField(max_length=20)

	def GetDuration(self):
		return self.Duration + " medicine"

	def GetPrice(self):
		price = str(self.Price)

		if len(price) > 3:
		    price = price[-len(price):-3]+","+price[-3::]

		if len(price) > 6:
		    oldprice = "," + price.split(",")[1]
		    price = price.split(",")[0]
		    price = price[::-1]
		    newprice = ''
		    for i in range(0, len(price), 1):
		        sta = price[i]
		        if((i-1) % 2 == 0):
		            sta += ","
		        newprice += sta
		    price = newprice[::-1].lstrip(",") + oldprice

		return "INR " + price + "/-"

class Day(models.Model):
	Date = models.DateField(default=datetime_date, primary_key=True)

	def GetDate(self):
		return self.Date.strftime('%Y-%m-%d')

class Slot(models.Model):
	PatientTreatment = models.ForeignKey(PatientTreatment, null=True, blank=True, on_delete=models.CASCADE, related_name="PatientTreatment")
	DateAlloted = models.ForeignKey(Day, on_delete=models.CASCADE, related_name="DateAlloted")
	TimeAlloted = models.TimeField(default=datetime_time)
	Description = models.TextField(null=True, blank=True)
	Package = models.ForeignKey(Package, null=True, blank=True, on_delete=models.CASCADE, related_name="Package")
	PaymentMade = models.BooleanField(default=False)
	PaymentReceipt = models.TextField(null=True, blank=True)

	def GetSlotValue(self):
		return f'{GetDateString(self.DateAlloted.Date)} : {GetTimeString(datetime.datetime.combine(self.DateAlloted.Date, self.TimeAlloted))}'

	def GetSlotDescription(self):
		time = datetime.datetime.combine(self.DateAlloted.Date, self.TimeAlloted)
		till = time + datetime.timedelta(hours=1)
		return f'{GetTimeString(time)} to {GetTimeString(till)}'