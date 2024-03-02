from django.db import models
from django.db.models.functions import Length

# Register __length transform as per Length documentation
models.CharField.register_lookup(Length)

class News(models.Model):
    caption = models.CharField('заголовок новости', max_length=95)
    annotation = models.CharField('заголовок новости', max_length=300)
    full_text = models.TextField('полный текст новости')
    last_name = models.CharField('фамилия', max_length=30)
    address = models.CharField('адрес', max_length=60)
    phone_number = models.CharField('номер телефона пользователя', max_length=11)
    is_public = models.BooleanField('для открытой печати', default=False)
    img_url = models.CharField('заголовок новости', max_length=300, null=True)
    updated_at = models.DateTimeField(auto_now=True)    
    created_at = models.DateTimeField(auto_now_add=True)  
    class Meta:
        db_table = "news"
        ordering = ['-updated_at']
        constraints = [
            models.CheckConstraint(
                check=models.Q(phone_number__length__gte=11),
                name="%(app_label)s_%(class)s_phone_number_length",
            )
        ]
