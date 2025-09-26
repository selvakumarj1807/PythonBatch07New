from django.shortcuts import render

from app.models import Doctor

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def doctors(request):
    doctors = Doctor.objects.filter(status=0)
    return render(request, 'doctors.html', {'doctors': doctors})