from django.shortcuts import render, redirect
from django.contrib import messages

import uuid
import commonfunctions
from .models import Day, Slot
import datetime

from main.views import ProfilePage
from main.models import Patient

def GetTimestampFromString(date, time):
	date = datetime.datetime.strptime(date, "%Y-%m-%d").date()

	time = time.split(":", 1)[1].split("to")[0].lstrip().rstrip()
	time = datetime.datetime.strptime(time, commonfunctions.time_string_format).time()

	timestamp = datetime.datetime.combine(date, time)
	return timestamp

def ConsultationPage(request):
	if request.method == "POST":

		Timestamp = GetTimestampFromString(request.POST['slot-date'], request.POST['slot-time'])

		name = request.POST['Name'].split(' ', 1)
		first_name = name[0]
		last_name = name[1] if len(name) > 1 else ''

		email = request.POST['Email']

		try:
			user = commonfunctions.User.objects.get(username=request.POST['Number'])
		except:
			password = 'userpassword' #str(uuid.uuid4())
			user = commonfunctions.User.objects.create_user(username=request.POST['Number'], first_name=first_name, last_name=last_name, email=email, password=password)
			user.save()
		finally:
			try:
				patient = commonfunctions.Patient.objects.get(User=user)
			except:
				patient = commonfunctions.Patient(User=user)
				patient.save()
		
		day = Day.objects.get(Date=Timestamp.date())
		slot = Slot.objects.get(DateAlloted=day, TimeAlloted=Timestamp.time())
		
		slot.Patient = patient
		slot.Description = request.POST['description']
		slot.Package = commonfunctions.Package.objects.get(Price=request.POST['package'])
		
		slot.save()

		messages.success(request, 'Slot Booked !')
		return redirect('/profile')

	slots = dict()

	for day in Day.objects.all():
		if (day.Date >= datetime.datetime.today().date()):
			slots[day] = Slot.objects.filter(DateAlloted=day, Patient=None)
	datelist = list(slots.keys())
	try:
		context = {
			'treatments':commonfunctions.Treatments(),
			'packages':commonfunctions.Packages(),
			'mindate':datelist[0],
			'maxdate':datelist[-1],
			'slots':slots,
		}
	except:
		context = {
			'treatments':commonfunctions.Treatments(),
			'packages':commonfunctions.Packages()
		}

	user = request.user
	if user.is_authenticated:
		context['name'] = user.get_full_name()
		context['number'] = user.username
		context['email'] = user.email

	return render(request, 'consultation/ConsultationPage.html', context)

def Plans(request):
	context = {
		'treatments':commonfunctions.Treatments(),
		'packages':commonfunctions.Packages(),
	}
	return render(request, 'consultation/Plans.html', context)