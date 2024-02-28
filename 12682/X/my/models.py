from django.db import models

class News(models.Model):
    caption = models.CharField('заголовок новости', max_length=100)
    full_text = models.TextField('полный текст новости')
    is_public = models.BooleanField('для открытой печати', default='ДА')
    updated_at = models.DateTimeField(auto_now=True)    
    class Meta :
        db_table = "news"
        ordering = ['-updated_at']
