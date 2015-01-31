from restfulAPI.models import Person, Meal, Location, Table
from rest_framework import serializers

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'contact_number', 'photo')

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('name', 'photo')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('latitude', 'longitude', 'address')

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ('host', 'attendance_num', 'available_num',
                  'attendance', 'menu', 'price', 'datetime',
                  'location', 'description', 'title',
                  'photo', 'pet', 'smoking', 'wine',
                  )
        depth = 2
