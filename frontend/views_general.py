from django.shortcuts import render, redirect
from database.models import *
import commonfunctions

from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib import auth

def testing(request):
    return render(request, 'testing.html')

def GetTimestampFromString(date, time):
    date = datetime.datetime.strptime(date, "%Y-%m-%d").date()

    time = time.split(":", 1)[1].split("to")[0].lstrip().rstrip()
    time = datetime.datetime.strptime(time, commonfunctions.time_string_format).time()

    timestamp = datetime.datetime.combine(date, time)
    return timestamp

class index(TemplateView):
    def get(self, request):
        # messages.info(request, 'Three credits remain in your account.')
        # messages.success(request, 'Profile details updated.')
        # messages.warning(request, 'Your account expires in three days.')
        # messages.error(request, 'Document deleted.')

        context = {
            'treatments':commonfunctions.Treatments(),
            'faqs':FAQ.objects.all(),
            'title':'Home'
        }

        return render(request, 'index.html', context)

    def post(self, request):
        print( request.POST )
        return redirect('/')

class treatments(TemplateView):
    def get(self, request):
        context = {
            'treatments':commonfunctions.Treatments(),
            'title':'All Treatments'
        }
        return render(request, 'general/treatments.html', context)

class treatment(TemplateView):
    def get(self, request, treatment):
        try:
            treatment = Treatment.objects.get(Name=treatment.replace("%2520", " ").rstrip().lstrip())
        except:
            return redirect(treatments)
        else:
            context = {
                'treatments':commonfunctions.Treatments(),
                'treatment':treatment,
                'title':f'Treatment for {treatment.Name}'
            }
            return render(request, 'general/treatment.html', context)

class consultation(TemplateView):
    def get(self, request):
        (slots, datelist) = commonfunctions.GetSlots()

        context = {
            'treatments':commonfunctions.Treatments(),
            'packages':commonfunctions.Packages(),
            'slots':slots,
            'datelist':datelist,
            'mindate':datelist[0],
            'maxdate':datelist[-1],
            'title':'Book Slot'
        }

        if 'selected_treatment' in request.GET:
            try:
                treatment = Treatment.objects.get(Name=request.GET['selected_treatment'])
                context['title'] += f" for {treatment.Name}"
                context['selected_treatment'] = treatment
            except:
                pass
        if 'selected_package' in request.GET:
            try:
                package = Package.objects.get(Price=request.GET['selected_package'])
                context['title'] += f" at {package.GetPrice()}"
                context['selected_package'] = package
            except:
                pass

        return render(request, 'general/consultation.html', context)

    def post(self, request):

        checklist = [
            'csrfmiddlewaretoken',
            'name',
            'number',
            'email',
            'gender',
            'age',
            'symptoms',
            'slot-date',
            'slot-time',
            'treatment-for',
            'package',
        ]

        for check in checklist:
            if check not in request.POST:
                messages.warning(request, f'{check} not provided')
                return redirect('/consultation')

        name = request.POST['name']
        name = name.split(' ', 1)
        number = request.POST['number']
        email = request.POST['email']
        gender = request.POST['gender']
        age = request.POST['age']
        symptoms = request.POST['symptoms']
        slot_date = request.POST['slot-date']
        slot_time = request.POST['slot-time']
        treatment_for = request.POST['treatment-for']
        package = request.POST['package']

        user = request.user
        if not user.is_authenticated:
            try:
                user = User.objects.get(username=number)
                messages.info(request, f'Seems like your account with {user.username} number already exists. Please login')
                return redirect('/consultation')
            except:
                make_new = True
            
            if email != '':
                try:
                    user = User.objects.get(email=email)
                    messages.info(request, f'Seems like your account with {email} email already exists. Please login')
                    return redirect('/consultation')
                except:
                    make_new = True

            if make_new:
                password = 'defaultpassword'
                first_name = name[0]
                last_name = name[1] if len(name) > 1 else ''
                user = User.objects.create_user(username=number, first_name=first_name, last_name=last_name, email=email, password=password, Gender=gender, Age=age)
                user.save()

        try:
            patient = Patient.objects.get(User=user)
        except:
            patient = Patient(User=user)
            patient.save()

        Timestamp = GetTimestampFromString(slot_date, slot_time)

        day = Day.objects.get(Date=Timestamp.date())
        slot = Slot.objects.get(DateAlloted=day, TimeAlloted=Timestamp.time())
        slot.Description = symptoms
        slot.Package = Package.objects.get(Price=package)

        try:
            patient_treatment = PatientTreatment.objects.filter(Patient=patient, Treatment=Treatment.objects.get(Name=treatment_for))[0]
        except:
            pass
            patient_treatment = PatientTreatment(Patient=patient)
            patient_treatment.save()

        try:
            patient_treatment.Treatment = Treatment.objects.get(Name=treatment_for)
        except:
            pass
        patient_treatment.Date = slot.DateAlloted.Date
        patient_treatment.Validity = slot.Package.Duration

        patient_treatment.save()

        slot.PatientTreatment = patient_treatment
        slot.save()

        messages.success(request, 'Slot Booked !')

        if user is not None and not request.user.is_authenticated:
            auth.login(request, user)
            # return redirect('/dashboard')
            return redirect(slot.Package.PaymentLink)
        else:
            return redirect('/login')

class plans(TemplateView):
    def get(self, request):
        context = {
            'treatments':commonfunctions.Treatments(),
            'title':'All Treatments',
            'packages':commonfunctions.Packages(),
        }
        return render(request, 'general/plans.html', context)