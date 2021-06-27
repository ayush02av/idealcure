from main.models import Treatment, Patient
from django.contrib.auth.models import User

def Treatments():
	return Treatment.objects.all()