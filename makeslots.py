import os, django
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'idealcure.settings')
django.setup()

try:
	os.system("rm db.sqlite3")
except:
    pass

# SuperUser generation
from django.contrib.auth.models import User
User.objects.create_user("admin", "admin@gmail.com", "adminadminadmin").save()

# FAQ generation
from main.models import FAQ

faqs = [
    {
        "question": "How does the online booking system work?",
        "answer": "Our online booking system allows you to schedule appointments with homeopathic doctors conveniently from the comfort of your home. Simply register on our platform, select a suitable time slot from the available options, and confirm your appointment. You'll receive confirmation details via email or SMS."
    },
    {
        "question": "What information do I need to provide during the booking process?",
        "answer": "To book an appointment, you'll need to provide basic information such as your name, contact details, any relevant medical history, and the reason for your visit. This helps our doctors better understand your needs before the consultation."
    },
    {
        "question": "Can I choose a specific homeopathic doctor for my appointment?",
        "answer": "Yes, you can select a preferred homeopathic doctor based on specialization or availability. Our platform allows you to browse through profiles of different doctors and choose the one that best suits your requirements."
    },
    {
        "question": "How far in advance can I book an appointment?",
        "answer": "Appointments can typically be scheduled several weeks in advance, depending on the availability of the doctors. However, we recommend booking at your earliest convenience to secure your preferred time slot."
    },
    {
        "question": "What if I need to reschedule or cancel my appointment?",
        "answer": "If you need to reschedule or cancel your appointment, you can do so through our platform. Please ensure to do this within a specified time frame to avoid any cancellation fees. You can find more details on our website or contact our support team for assistance."
    },
    {
        "question": "Are there any prerequisites before booking an appointment?",
        "answer": "Generally, there are no prerequisites before booking an appointment. However, for certain specialized consultations, you may be required to provide specific medical documents or undergo preliminary assessments. Our platform will guide you through any additional requirements if necessary."
    },
    {
        "question": "How do I pay for my appointment?",
        "answer": "We accept various payment methods, including online payment through secure gateways, insurance coverage (if applicable), and other convenient options. You can complete the payment process during the booking or consultation stage."
    },
    {
        "question": "What can I expect during my online consultation?",
        "answer": "During your online consultation, you'll have a one-on-one session with your chosen homeopathic doctor. The doctor will discuss your medical history, current symptoms, and any concerns you may have. They will then provide personalized recommendations and treatment plans tailored to your needs."
    },
    {
        "question": "Is my personal and medical information secure?",
        "answer": "Yes, we prioritize the security and confidentiality of your personal and medical information. Our platform employs robust encryption protocols and follows strict privacy policies to ensure that your data remains secure at all times."
    },
    {
        "question": "What if I encounter technical difficulties during the booking process?",
        "answer": "In case you encounter any technical difficulties while using our platform, our customer support team is here to assist you. You can reach out to us via email or phone, and we'll promptly address any issues or provide guidance to ensure a seamless booking experience."
    }
]

for faq in faqs:
    FAQ(Question = faq['question'], Answer = faq['answer']).save()

from consultation.models import Day, Slot

today = datetime.date.today()

days = [day for day in Day.objects.all() if day.Date<today]

slots = list()

#Deleting empty slots of those days earlier than TODAY
for day in days:
	slots += [slot for slot in Slot.objects.filter(DateAlloted=day, Patient=None)]
	Slot.objects.filter(DateAlloted=day, Patient=None).delete()
	if len(Slot.objects.filter(DateAlloted=day)) == 0:
		day.delete()

#Creating new slots from today onwards
for day in range(60):
	date = today + datetime.timedelta(hours=(24*(day)))
	if date.isoweekday() != 7:
		try:
			# if date.Date.isoweekday == 7:
			# 	continue
			Day(Date=date).save()
		except Exception as exception:
			pass
		finally:
			dayToBeAlloted = Day.objects.get(Date=date)
			for hour in range(5,9):
				try:
					slot = Slot.objects.get(DateAlloted=dayToBeAlloted, TimeAlloted=datetime.time(12+hour,0,0))
				except:
					Slot(DateAlloted=dayToBeAlloted, Patient=None, TimeAlloted=datetime.time(12+hour,0,0)).save()
				
				# try:
				# 	slot = Slot.objects.get(DateAlloted=dayToBeAlloted, Patient=None, TimeAlloted=datetime.time(hour,30,0))
				# except:
				# 	Slot(DateAlloted=dayToBeAlloted, Patient=None, TimeAlloted=datetime.time(hour,30,0)).save()