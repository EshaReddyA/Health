from django.db import models

# Create your models here.

class patients(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    
class doctors(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)