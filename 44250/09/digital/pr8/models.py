from django.db import models

class Client (models.Model):
    Name=models.CharField(max_length=255)
    Adress=models.CharField(max_length=255)
    Telephone_number=models.FloatField()
    Email=models.CharField(max_length=255)
    Gender=models.CharField(default='Укажите Ваш пол', max_length=255)

class Goods (models.Model):
    Product_name=models.CharField(max_length=255)
    Product_price=models.FloatField()
    Product_availability=models.CharField(max_length=255)

class Orders (models.Model):
    Order_date=models.DateField()
    Order_sum=models.FloatField()
    Number_of_products=models.FloatField()

class OnlineOrders (models.Model):
    Client_Name=models.ForeignKey(Client, on_delete=models.RESTRICT)
    Data_Time=models.ForeignKey(Orders, on_delete=models.RESTRICT)
    Product_type=models.ForeignKey(Goods, on_delete=models.RESTRICT)

    
    
