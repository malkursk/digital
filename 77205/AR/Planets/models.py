from django.db import models

class Planets(models.Model):
    name = models.CharField(max_length=255, unique = True)
    pic = models.CharField(max_length=1000)
    about = models.CharField(max_length=1000)
    orbital_period = models.IntegerField()
    radius = models.FloatField()
    weight = models.FloatField()
    image = models.ImageField(blank=True, upload_to='images')

# Create your models here.
