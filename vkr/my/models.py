from django.db import models
from django.contrib.auth import get_user_model 
import uuid

class Sport(models.Model): # виды спорта
    DICT = (
        ('Фигурное катание',''),
        ('Синхронное плавание',''),
        ('Пляжный волейбол',''),
        ('Прыжки в воду',''),
        ('Фигурное катание',''),
        ('Спортивная гимнастика','')
    )    
    name = models.CharField(choices=DICT, max_length=50, unique = True)

class Game(models.Model): # олимпийские игры
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4)       
    country = models.CharField(max_length=255)
    date_from = models.DateField()
    date_to = models.DateField()

class News(models.Model): # новости
    caption = models.CharField(max_length=50)
    text = models.TextField()
    phone_number = models.CharField(max_length=50)
    borrower = models.ForeignKey(get_user_model(), on_delete=models.RESTRICT)
    enabled = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Person(models.Model): # участники игр
    first_name = models.CharField(max_length=50)      
    last_name = models.CharField(max_length=50)
    born = models.DateField()
    address = models.CharField(max_length=255)  

class Winner(models.Model): # призёры
    DICT = (
        (1, 'I место, золото'),
        (2, 'II место, серебро'),
        (3, 'III место, бронза'),
    )
    place = models.IntegerField(choices=DICT)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    class Meta:        
        unique_together = ('game', 'person')
    
    
