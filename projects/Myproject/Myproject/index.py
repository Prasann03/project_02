# yourappname/views.py
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import MedicationForm
from .models import Medication
from . import models
def home(request):
    return render(request, 'home.html')

def Disclaimer(request):
    return render(request, 'Disclaimer.html')

def searching(request):
    return render(request, 'searching.html')

def info(request):  
    if request.method=="POST":
        form =MedicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info')
    else:
        form = MedicationForm()

    medicines = Medication.objects.all()
    return render(request, 'info.html', {'form': form, 'medicines': medicines})

def successful_profile(request):
    return render(request, 'successful_profile.html')

def loginsuccess(request):
    return render(request, 'loginsuccess.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def App_page(request):
    return render(request, 'App_page.html')

def page_detail(request,id):
    page=models.Pages.objects.get(id=id)
    return render(request,'page.html',{'page':page})