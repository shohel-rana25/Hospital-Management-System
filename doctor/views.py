from django.shortcuts import render
from rest_framework import viewsets, filters, pagination
from .import models
from .import serializers

# Create your views here.
class DoctorPagination(pagination.PageNumberPagination):
       page_size=1;
       page_size_query_param=page_size
       max_page_size=100


class DoctorViewset(viewsets.ModelViewSet):
       queryset = models.DoctorModel.objects.all()
       serializer_class =serializers.DoctorSerializer
       filter_backends=[filters.SearchFilter]
       pagination_class=DoctorPagination
       search_fields=['user__first_name', 'user__last_name', 'designation__name', 'specialization__name', 'available_time__name', 'fee__name']


class SpecializationViewset(viewsets.ModelViewSet):
       queryset = models.SpecializationModel.objects.all()
       serializer_class =serializers.SpecializationSerializer

class DesignationViewset(viewsets.ModelViewSet):
       queryset = models.DesignationModel.objects.all()
       serializer_class =serializers.DesignationSerializer

class ReviewViewset(viewsets.ModelViewSet):
       queryset = models.ReviewModel.objects.all()
       serializer_class =serializers.ReviewModelSerializer

class AvailableTimeViewset(viewsets.ModelViewSet):
       queryset = models.AvailableTimeModel.objects.all()
       serializer_class =serializers.AvailableTimeSerializer
