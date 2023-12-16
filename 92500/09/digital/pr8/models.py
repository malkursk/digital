from django.db import models

class Pacient (models.Model):
    Name=models.CharField(max_length=255)
    Breed=models.CharField(max_length=255)
    Age=models.FloatField()
    Gender=models.CharField(max_length=255)
    Owner=models.CharField(max_length=255)

class Owner(models.Model):
    Name=models.CharField(max_length=255)
    Telephone_number=models.FloatField()
    Address=models.CharField(max_length=255)
    Gender=models.CharField(default='Введите Ваш пол', max_length=255 )

class Doctor(models.Model):
    Name=models.CharField(max_length=255)
    Specialization=models.CharField(max_length=255)
    Working_hours=models.TimeField()

class Reception(models.Model):
    Date_Time=models.ForeignKey(Doctor, on_delete=models.RESTRICT)
    Pacient=models.ForeignKey(Pacient, on_delete=models.RESTRICT)
    Session_Time=models.DateTimeField()
    



    
