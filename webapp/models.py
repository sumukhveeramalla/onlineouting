from django.db import models
from django.forms import BooleanField
from django.db import models
import datetime
# Create your models here.


# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    rollnumber = models.IntegerField()
    description = models.TextField()
    prefer = models.CharField(max_length=10)
    Residence = models.CharField(max_length=100)
    year = models.CharField(max_length=30)
    phoneNo = models.CharField(max_length=10)