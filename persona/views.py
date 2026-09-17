from django.shortcuts import render
from rest_framework import viewsets
from .models import Person
from .serializers import PersonSerializer

# Create your views here.

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by("-id")
    serializer_class = PersonSerializer