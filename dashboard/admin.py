from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import WeatherData,Location

admin.site.register(WeatherData)
admin.site.register(Location)
