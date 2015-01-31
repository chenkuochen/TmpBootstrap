from django.shortcuts import render

# Create your views here.
from restfulAPI.models import Person, Meal, Location, Table
from rest_framework import viewsets
from restfulAPI.serializers import TableSerializer, MealSerializer


class TableViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class MealViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
