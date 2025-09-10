from django.contrib import admin

from app.models import Category, Product

# Register your models here.

admin.site.register(Product)

admin.site.register(Category)