from django.shortcuts import render

# Create your views here.

def app02Index(request):
    return render(request, 'app02/index.html')