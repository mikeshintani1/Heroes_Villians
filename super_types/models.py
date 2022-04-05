from django.db import models

# Create your models here.
class Super_Types(models.Model):
    type = models.CharField(max_length=255)
   
class Power(models.Model):
    name = models.CharField(max_length=255)

