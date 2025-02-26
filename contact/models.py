from django.db import models

# Create your models here.

class ContactModel(models.Model):
    name=models.CharField(max_length=25)
    phone=models.IntegerField()
    problem=models.TextField()

    def __str__(self):
            return self.name 
        