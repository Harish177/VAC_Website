from django.db import models

# Create your models here.


class Join(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    RegNo = models.CharField(max_length=8)
    Year = models.DecimalField(max_digits=1, decimal_places=0)
    DateOfBirth = models.DateField()
    Department = models.CharField(max_length=50)
    MobileNumber = models.DecimalField(max_digits=10, decimal_places=0)
    AreaOfInterest = models.CharField(max_length=100)
