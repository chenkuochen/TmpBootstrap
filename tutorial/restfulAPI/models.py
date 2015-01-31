from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)
    contact_number = models.CharField(max_length=30)
    photo = models.FileField()

class Meal(models.Model):
    name = models.CharField(max_length=30)
    photo = models.FileField()

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=100)

class Table(models.Model):
    host = models.ForeignKey(Person)
    attendance_num = models.IntegerField()
    available_num = models.IntegerField()
    attendance = models.ManyToManyField(Person, related_name='attendance_table')
    menu = models.ManyToManyField(Meal)
    price = models.IntegerField()
    datetime = models.DateTimeField()
    location = models.ForeignKey(Location)
    description = models.CharField(max_length=500)
    title = models.CharField(max_length=50)
    photo = models.FileField()
    pet = models.BooleanField(default=False)
    smoking = models.BooleanField(default=False)
    wine = models.BooleanField(default=False)
    #meal_type
