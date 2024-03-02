from django.db import models

class News(models.Model):
    caption = models.CharField('заголовок новости', max_length=100)
    full_text = models.TextField('полный текст новости')
    last_name = models.CharField('фамилия', max_length=30)
    address = models.CharField('адрес', max_length=60)
    phone_number = models.CharField('номер телефона пользователя', max_length=12)
    is_public = models.BooleanField('для открытой печати', default=False)
    updated_at = models.DateTimeField(auto_now=True)    
    class Meta:
        db_table = "news"
        ordering = ['-updated_at']
