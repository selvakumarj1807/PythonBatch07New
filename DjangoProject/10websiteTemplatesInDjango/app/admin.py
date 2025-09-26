from django.contrib import admin

# Register your models here.

from .models import Appoitment, Doctor

admin.site.register(Doctor)

admin.site.register(Appoitment)