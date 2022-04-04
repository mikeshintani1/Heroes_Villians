from django.db import models

import super_types

# Create your models here.
class Supers(models.Model):
    name = models.CharField(max_length=255)
    alter_ego = models.CharField(max_length=255)
    primary_ability = models.CharField(max_length=255)
    secondary_ability = models.CharField(max_length=255)
    catchphrase = models.CharField(max_length=255)
    super_type = models.ForeignKey(super_types, on_delete=models.CASCADE)