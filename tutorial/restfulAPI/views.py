from django.shortcuts import render

# Create your views here.
from restfulAPI.models import Person, Meal, Location, Table
from rest_framework import viewsets
from restfulAPI.serializers import TableSerializer, MealSerializer, LocationSerializer, PersonSerializer

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
