import os, django, datetime

applist = [
	'main',
	'consultation'
]

def clearscreen():
	try:
		os.system('cls')
	except:
		os.system('clear')

root = os.getcwd()

clearscreen()

if True:#input('Enter admin password first : ') == 'admin':
	try:
		os.remove('db.sqlite3')
	except:
		pass

	for app in applist:
		path = root + '/' + app + '/migrations'
		os.chdir(path)
		
		for file in os.listdir():
			if file.split('.')[-1] == 'py' and file != '__init__.py':
				os.remove(file)

	os.chdir(root)

	try:
		os.system('rmdir /s /q media')
	except:
		os.system('rm -f -r media')
	finally:
		os.mkdir('media')

	os.system('python manage.py makemigrations')
	os.system('python manage.py migrate')

	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'idealcure.settings')
	django.setup()

	from django.contrib.auth.models import User

	admin = User.objects.create_user(username='admin', first_name='Admin', email='theidealcureclinic@gmail.com', password='admin')
	admin.is_superuser = True
	admin.is_staff = True
	admin.save()
	print('Admin Added')

	from django.contrib.auth.models import Group, Permission

	developer_group, created = Group.objects.get_or_create(name="Developer")

	permissionList = []
	
	permissionList.append(Permission.objects.get(codename='add_faq'))
	permissionList.append(Permission.objects.get(codename='change_faq'))
	permissionList.append(Permission.objects.get(codename='delete_faq'))
	permissionList.append(Permission.objects.get(codename='view_faq'))

	permissionList.append(Permission.objects.get(codename='add_treatment'))
	permissionList.append(Permission.objects.get(codename='change_treatment'))
	permissionList.append(Permission.objects.get(codename='delete_treatment'))
	permissionList.append(Permission.objects.get(codename='view_treatment'))
	print('Developer Group added')

	for permission in permissionList:
		developer_group.permissions.add(permission)

	ayush_developer = User.objects.create_user(username='ayush_developer', first_name='Ayush', last_name='Developer', email='ayush02av@gmail.com', password='@AWebDeveloperNeedsCoding@')
	ayush_developer.is_staff = True
	ayush_developer.save()

	developer_group.user_set.add(ayush_developer)
	print('Developer User added')

	from main.models import Treatment, FAQ, Package

	treatmentList = {
		'White Spots':'White Spots is a disease',
		'Psoriasis':'Psoriasis is a disease'
	}

	for treatment in treatmentList:
		Treatment(Name=treatment, Description=treatmentList[treatment]).save()
	print('Treatments Added')

	faqList = {
		'How is Ideal Cure Homoeopathy & Wellness Clinic different.': 'It is different & unique because each case is studied in depth & individualized  as per the need of the patient. Medicines are selected strictly according to the core principles of Homoeopathy, which have stood the test of time for hundreds of years. Each patient is guided about the correct diet & lifestyle also along with medication. Apart from this, each & every query of yours is answered in detail.',
		'How do I take a consultation & discuss my problems with Dr. Rashmi?': 'Simply fill in your details, select the date and time of your choice, make payment & your slot will be booked.\r\nYou can discuss your case in the booked slot through normal voice call or WhatsApp video call.\r\nYou are requested to call only from the mobile number which you have provided.',
		'How do I receive my medicines after the consultation?': 'After your case-discussion, your individualized medicines along with all instructions as to how to take them can be sent to your address through courier within shortest possible time.',
		'What is the quality of medicines used by your clinic?': 'Rest assured. Only the highest quality German Homoeopathic medicines are given to the patients at Ideal Cure Homoeo Clinic.',
		'I am already taking many types of Allopathic medicines without much relief. Do I need to stop them immediately?': 'No, you need not. When your treatment starts, the other medicines will be gradually tapered off as per the need of your case. MINIMUM medicines & MAXIMUM relief is our motto.',
		'Why should I take Homoeopathic treatment for my ailments? Isn\'t it a slow-acting system?': 'After a case is studied well, the most perfect medicine(s) selected on the basis of totality of symptoms of the patient, acts like a charm in most cases & relief is obtained within a very short period of time. However, in some chronic & multiple diseases, the medicines do take some time to act.',
		'How to consume the medicines?': 'These medicines should be consumed when your mouth is fresh, does not have any odor or smell of anything which you might have eaten a few minutes ago. One should avoid strong smelling items such as garlic, onion etc while taking Homoeopathic treatment.'
	 }

	for faq in faqList:
		FAQ(Question=faq, Answer=faqList[faq]).save()
	print('FAQs Added')

	packageList = {
		'250':['Single Time', 'Suitable for those who are having some acute problem or are seeking a second opinion for their treatment.<br><b>Can be converted to other plans if needed.</b>'],
		'500':['10 days', 'Consultation fee waived off.'],
		'1000':['20 days', 'Consultation fee waived off.'],
		'1400':['30 days', 'Consultation fee waived off.'],
		'4000':['3 months', 'Consultation fee waived off.<br><b>Unlimited consultation, follow ups and medicines.</b>'],
		'7000':['6 months', 'Consultation fee waived off.<br><b>Unlimited consultation, follow ups and medicines.</b>'],
		'12000':['1 years', 'Consultation fee waived off.<br><b>Unlimited consultation, follow ups and medicines.</b>']
	}

	for package in packageList:
		Package(int(package), packageList[package][0], packageList[package][1]).save()

	import makeslots
	makeslots.MakeSlots()
	print('Slots Added')

	input("\nEnter to run server...")

	clearscreen()
	os.system('python manage.py runserver')
else:
	input('Wrong Password!!!')