from django.shortcuts import render
import commonfunctions
from django.contrib.auth.models import User

from consultation.models import Slot

def AdminPanelOverviewPage(request):
	context = {
		'treatments':commonfunctions.Treatments(),
		'PendingSlots':Slot.objects.exclude(Patient=None)
	}

	return render(request, 'adminpanel/OverviewPage.html', context)
