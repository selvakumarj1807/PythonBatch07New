from django.shortcuts import render

# Create your views here.

from rest_framework import generics

from app.serializers import StudentSerializer
from .models import Student

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer