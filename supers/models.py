from django.db import models
from super_types.models import Power
from super_types.models import Super_Types

# Create your models here.
class Supers(models.Model):
    name = models.CharField(max_length=255)
    alter_ego = models.CharField(max_length=255)
    # primary_ability = models.ManyToManyField(Power, related_name='power')
    # secondary_ability = models.ManyToManyField(Power, related_name='powers')
    catchphrase = models.CharField(max_length=255)
    super_types = models.ForeignKey(Super_Types, on_delete=models.CASCADE)
   
    power_ability = models.ManyToManyField(Power)