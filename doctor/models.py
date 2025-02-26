from django.db import models
from django.contrib.auth.models import User
from patient.models import PatientModel

# Create your models here.

class SpecializationModel(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)  # Changed to SlugField for better URL compatibility

    def __str__(self):
        return self.name

class DesignationModel(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)  # Changed to SlugField

    def __str__(self):
        return self.name

class AvailableTimeModel(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class DoctorModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Fixed ForeignKey issue
    image = models.ImageField(upload_to="doctor/images/")
    specialization = models.ManyToManyField(SpecializationModel)
    designation = models.ManyToManyField(DesignationModel)
    available_time = models.ManyToManyField(AvailableTimeModel)  # Removed `on_delete`
    fee = models.IntegerField()
    meet_link = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"  # Added space for readability

STAR_CHOICES = [
    ('🌟','🌟'),
    ('🌟🌟','🌟🌟'),
    ('🌟🌟🌟','🌟🌟🌟'),
    ('🌟🌟🌟🌟','🌟🌟🌟🌟'),
    ('🌟🌟🌟🌟🌟','🌟🌟🌟🌟🌟'),
]

class ReviewModel(models.Model):
    reviewer=models.ForeignKey(PatientModel, on_delete=models.CASCADE)
    doctor=models.ForeignKey(DoctorModel, on_delete=models.CASCADE)
    description=models.TextField()
    time=models.DateTimeField(auto_now_add=True)
    rating=models.CharField(choices=STAR_CHOICES, max_length=10)
    
    def __str__(self):
        return f"Patient{self.reviewer.user.first_name} ;Doctor{self.doctor.user.first_name}"