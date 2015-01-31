from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)
    contact_number = models.CharField(max_length=30)
    photo = models.FileField(blank=True)

    def __unicode__(self):
        return 'name=%s, contact_number=%s' % (self.name, self.contact_number)

class Meal(models.Model):
    name = models.CharField(max_length=30)
    photo = models.FileField(blank=True)

    def __unicode__(self):
        return '%s' % (self.name)

class Location(models.Model):
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    address = models.CharField(max_length=100)

    def __unicode__(self):
        return '%s (%s, %s)' % (self.address, self.longitude, self.latitude)

class Table(models.Model):
    host = models.ForeignKey(Person)
    attendance_num = models.IntegerField()
    available_num = models.IntegerField(null=True, blank=True)
    attendance = models.ManyToManyField(Person, related_name='attendance_table', blank=True)
    menu = models.ManyToManyField(Meal, blank=True)
    price = models.IntegerField()
    datetime = models.DateTimeField()
    location = models.ForeignKey(Location)
    description = models.CharField(max_length=500, blank=True)
    title = models.CharField(max_length=50)
    photo = models.FileField(blank=True)
    pet = models.BooleanField(default=False)
    smoking = models.BooleanField(default=False)
    wine = models.BooleanField(default=False)
    #meal_type
    
