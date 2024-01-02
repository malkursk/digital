from django.db import models
from django.core.validators import MinLengthValidator

class Account(models.Model):
    login = models.CharField(max_length=25, unique=True, verbose_name='логин')
    passw = models.CharField(max_length=25, validators=[MinLengthValidator(3)], verbose_name='пароль')    
    busy = models.BooleanField(verbose_name='выдана', null=True, default=False)
    fio = models.CharField(max_length=255, null=True, verbose_name='ФИО')
    phone = models.CharField(max_length=20, null=True, verbose_name='контактный телефон')
    org = models.CharField(max_length=255, null=True, verbose_name='название организации')
    region = models.CharField(max_length=255, null=True, default='Курск',verbose_name='область (город)')
    comment = models.CharField(max_length=255, null=True, verbose_name='комментарий')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta :
        db_table = "account"
        verbose_name_plural = 'Учетные записи'
        verbose_name = 'Учетная запись'
        ordering = ['-updated_at']

class Test(models.Model):
    info = models.CharField(verbose_name='информация', max_length=255)
    enable = models.BooleanField(verbose_name='доступна', null=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    class Meta :
        db_table = "test"
        ordering = ['-updated_at']
