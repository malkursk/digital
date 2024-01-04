from django.db import models
from django.core.validators import MinLengthValidator

class Account(models.Model):
    login = models.CharField('логин', max_length=25, unique=True)
    passw = models.CharField('пароль', max_length=25, validators=[MinLengthValidator(3)])    
    busy = models.BooleanField('выдана', default=False)
    fio = models.CharField('ФИО',max_length=255, null=True)
    phone = models.CharField('телефон',max_length=20, null=True)
    org = models.CharField('организация',max_length=255, null=True)
    region = models.CharField('область (город)', max_length=255, null=True, default='Курск')
    comment = models.CharField('комментарий',max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta :
        db_table = "account"
        verbose_name_plural = 'Учетные записи'
        verbose_name = 'Учетная запись'
        ordering = ['-updated_at']

class Test(models.Model):
    info = models.CharField('информация', max_length=255)
    enable = models.BooleanField('доступно?', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    class Meta :
        db_table = "test"
        ordering = ['-updated_at']
