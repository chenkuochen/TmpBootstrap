from django.contrib import admin
from restfulAPI.models import Person, Meal, Location, Table

# Register your models here.
admin.site.register(Person)
admin.site.register(Meal)
admin.site.register(Location)
admin.site.register(Table)
