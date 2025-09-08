from django.shortcuts import render

# Create your views here.

def app01Index(request):
    return render(request, 'app01/index.html')