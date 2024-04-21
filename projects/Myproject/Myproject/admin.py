from django.contrib import admin
from .models import User
from .models import Medication
from . import models

admin.site.register(User)
admin.site.register(Medication)

class MedicationAdmin(admin.ModelAdmin):
    list_display = ('medicine_name', 'dosage_count', 'date_taken')

