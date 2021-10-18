from django.contrib import admin
from . import models

admin.site.register(models.User)
admin.site.register(models.Treatment)
admin.site.register(models.Patient)
admin.site.register(models.PatientTreatment)
admin.site.register(models.PatientRecord)
admin.site.register(models.PatientFile)
admin.site.register(models.FAQ)
admin.site.register(models.Package)
admin.site.register(models.Day)
admin.site.register(models.Slot)