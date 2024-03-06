from django.db import models

class News(models.Model):
    caption = models.CharField('заголовок новости', max_length=100)
    full_text = models.TextField('полный текст новости') 
    last_name = models.CharField('Фамилия', max_length=30)
    adress = models.CharField('Адес', max_length=100)
    phone_number = models.CharField(' Номер телефон', max_length=13)
    is_public = models.BooleanField('для открытой печати', default=False)
    updated_at = models.DateTimeField(auto_now=True)    
    class Meta :
        db_table = "news"
        ordering = ['-updated_at']
