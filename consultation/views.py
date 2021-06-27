from django.shortcuts import render, redirect
from django.contrib import messages

import uuid
import commonfunctions
from .models import Day, Slot
import datetime

from main.views import ProfilePage
from main.models import Patient

def ConsultationPage(request):

	if request.method == "POST":

		Timestamp = datetime.datetime.strptime(request.POST['slot-date']+' '+request.POST['slot-time'].split(' -')[0], '%Y-%m-%d %H:%M')

		name = request.POST['Name'].split(' ', 1)
		first_name = name[0]
		last_name = name[1] if len(name) > 1 else ''

		email = request.POST['Email']

		try:
			user = commonfunctions.User.objects.get(username=request.POST['Number'])
		except:
			password = 'awebdevneedscoding' #str(uuid.uuid4())
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
		slot.save()
		messages.success(request, 'Slot Booked !')
		return redirect('/profile')

	slots = dict()

	for day in Day.objects.all():
			if not(day.Date >= datetime.datetime.today().date()):
					continue
			else:
				slots[day] = list()
				for slot in Slot.objects.filter(DateAlloted=day, Patient=None):
					slot.Description = slot.TimeAlloted.__str__()[:-3] + ' - ' + ( datetime.datetime.combine(slot.DateAlloted.Date, slot.TimeAlloted) + datetime.timedelta(hours=1) ).time().__str__()[:-3]
					slots[day].append(slot)
	datelist = list(slots.keys())
	try:
		context = {
			'treatments':commonfunctions.Treatments(),
			# 'days':Day.objects.all(),
			# 'slots':Slot.objects.all()
			'mindate':datelist[0],
			'maxdate':datelist[-1],
			'slots':slots,
		}
	except:
		context = {
			'treatments':commonfunctions.Treatments(),
		}

	user = request.user
	if user.is_authenticated:
		if len(Patient.objects.filter(User=user)) != 0:
			context['name'] = user.get_full_name()
			context['number'] = user.username
			context['email'] = user.email

	return render(request, 'consultation/ConsultationPage.html', context)