from django.contrib import admin

# Register your models here.
from .models import Hero, City

admin.site.register(Hero)
admin.site.register(City)
