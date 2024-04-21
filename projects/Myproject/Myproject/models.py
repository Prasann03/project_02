from django.db import models
from datetime import date

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)

class Medication(models.Model):
    medicine_name = models.CharField(max_length=255)
    dosage_count = models.IntegerField(default=0)
    date_taken = models.DateField(default=date(1900, 1, 1)) # Set default to today's date
    
    def __str__(self):
        return f'{self.medicine_name} - {self.date_taken}'


