def MakeSlots():	
	import os, django

	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'idealcure.settings')
	django.setup()

	from consultation.models import Day, Slot
	import datetime

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
	for day in range(8):
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
						slot = Slot.objects.get(DateAlloted=dayToBeAlloted, TimeAlloted=datetime.time(hour,0,0))
					except:
						Slot(DateAlloted=dayToBeAlloted, Patient=None, TimeAlloted=datetime.time(hour,0,0)).save()
					
					# try:
					# 	slot = Slot.objects.get(DateAlloted=dayToBeAlloted, Patient=None, TimeAlloted=datetime.time(hour,30,0))
					# except:
					# 	Slot(DateAlloted=dayToBeAlloted, Patient=None, TimeAlloted=datetime.time(hour,30,0)).save()

if __name__ == "__main__":
	MakeSlots()