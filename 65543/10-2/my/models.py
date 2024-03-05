from django.db import models

class News(models.Model):
    caption = models.CharField('заголовок новости', max_length=100)
    is_public = models.BooleanField('для открытой печати', default=False)
    updated_at = models.DateTimeField(auto_now=True)  
    last_name = models.CharField('Фамилия', max_length=30)
    address = models.CharField('Адрес', max_length=60)
    phon_number = models.CharField('номер телефона пользователя', max_length=12)  
    full_text = models.TextField('текст новости')
    
    class Meta :
        db_table = "news"
        ordering = ['-updated_at']
