from django.contrib import admin
from .models import HouseDataPoint , HousingQueryData ,ListOfCities
# Register your models here.

admin.site.register(HousingQueryData)
admin.site.register(HouseDataPoint)
admin.site.register(ListOfCities)