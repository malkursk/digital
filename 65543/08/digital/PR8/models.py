from django.db import models

# Create your models here.

class Game(models.Model): 
    place = models.CharField(max_length=255) 
    dateFrom = models.DateField()  
    dateTo = models.DateField()  
 
class Sport(models.Model): 
    name = models.CharField(max_length=50) 
 
class Person(models.Model): 
    fio = models.CharField(max_length=50) 
    born = models.DateField() 
 
class Winner(models.Model): 
    medal = models.IntegerField() 
    game = models.ForeignKey(Game, on_delete=models.RESTRICT) 
    sport = models.ForeignKey(Sport, on_delete=models.RESTRICT) 
    person = models.ForeignKey(Person, on_delete=models.RESTRICT)
    