from django.shortcuts import render, redirect
from .models import Treatment, FAQ, Patient
import commonfunctions
from django.contrib.auth.models import User
from consultation.models import Slot

def HomePage(request):
	context = {
		'treatments':commonfunctions.Treatments(),
		'faqs':FAQ.objects.all()
	}

	return render(request, 'main/HomePage.html', context)

def TreatmentsPage(request, treatmentFor):
	context = {
		'treatments':commonfunctions.Treatments(),
	}
	# if treatmentFor != 'all':

	treatmentName = treatmentFor
	treatmentName = treatmentName.split("%2520")
	treatmentFor = ''
	for i in treatmentName:
	    treatmentFor += i + ' '
	treatmentFor = treatmentFor.rstrip()
	
	context['treatmentFor'] = Treatment.objects.filter(Name=treatmentFor)[0]

	return render(request, 'main/TreatmentsPage.html', context)

def Profile(request):
	if request.user.is_authenticated:
		return redirect(f'/profile/{request.user}')
	else:
		return redirect('login')

def ProfilePage(request, username):
	try:
		if request.user == User.objects.get(username=username):
			context = {
				'treatments':commonfunctions.Treatments(),
			}
			if request.user.is_superuser:
				context['staff_links'] = ['backend', 'adminpanel']
			elif request.user.is_staff:
				context['staff_links'] = ['backend']
			else:
				patient = Patient.objects.get(User=User.objects.get(username=username))
				context['patient_info'] = {
					'Name':patient.User.get_full_name(),
					'Number':patient.User.username,
					'Age':patient.Age,
					'Address':patient.Address,
				}
				context['Slots'] = Slot.objects.filter(Patient=patient)
			return render(request, 'main/ProfilePage.html', context)
		else:
			return redirect(Profile)
	except:
		return redirect(Profile)

def TNC(request):
	return render(request, 'main/tnc.html', {'treatments':commonfunctions.Treatments()})

def Privacy(request):
	return render(request, 'main/privacy.html', {'treatments':commonfunctions.Treatments()})