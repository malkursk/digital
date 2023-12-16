from django.db import models

class games (models.Model):
    city = models.CharField(max_length=245)
    datefrom = models.DateField()
    dateto = models.DateField()
    win_coynty = models.TextField(default='Победила дружба')

class sportsmen (models.Model):
    name = models.CharField(max_length=30)
    country = models.DateField()
    age = models.DateField()

class sport_type (models.Model):
    sport = models.CharField(max_length=35)

class result (models.Model):
    place = models.IntegerField()
    person = models.ForeignKey(sportsmen, on_delete=models.RESTRICT)
    sport = models.ForeignKey(sport_type, on_delete=models.RESTRICT)
    game = models.ForeignKey(games, on_delete=models.RESTRICT)
