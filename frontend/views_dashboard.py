from django.shortcuts import render, redirect
from database.models import *
import commonfunctions

from django.views.generic import TemplateView
from django.contrib import auth

def get_context(request):
    return {
        'title':request.user.get_full_name(),
        'show_header_footer':True,
    }

def get_patient(request):
    return Patient.objects.get(User=request.user)

def get_treatment_list(request):
    if not request.user.is_superuser:
        return PatientTreatment.objects.filter(Patient=get_patient(request))
    else:
        return PatientTreatment.objects.filter(ClosedStatus=False)

def get_slot_list(request, treatment_list=None):
    treatment_list = treatment_list if treatment_list != None else get_treatment_list(request)
    return Slot.objects.filter(PatientTreatment__in=treatment_list)

# def pending_payment_slot(request):
#     user = request.user

class dashboard(TemplateView):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/login')

        context = get_context(request)

        treatment_list = get_treatment_list(request)
        context['highlights'] = [
            {"key":"Ongoing Treatments", "value":len(treatment_list) },
            {"key":"Pending Slots", "value":len(get_slot_list(request, treatment_list)) },
        ]

        return render(request, 'dashboard/index.html', context)

class dashboard_ongoing_treatments(TemplateView):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/login')

        context = get_context(request)
        context['patient_treatment_list'] = get_treatment_list(request)

        return render(request, 'dashboard/ongoingtreatments.html', context)

class dashboard_pending_slots(TemplateView):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/login')

        context = get_context(request)
        context['slot_list'] = get_slot_list(request)

        return render(request, 'dashboard/pendingslots.html', context)