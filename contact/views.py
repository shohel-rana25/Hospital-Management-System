from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializers
# Create your views here.

class ContactViewset(viewsets.ModelViewSet):
       queryset = models.ContactModel.objects.all()
       serializer_class =serializers.ContactSerializer