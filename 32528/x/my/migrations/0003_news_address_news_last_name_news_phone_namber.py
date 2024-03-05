# Generated by Django 5.0.3 on 2024-03-05 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my', '0002_news_full_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='address',
            field=models.CharField(default=1, max_length=70, verbose_name='адрес'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='last_name',
            field=models.CharField(default=1, max_length=50, verbose_name='фамилия'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='phone_namber',
            field=models.CharField(default=1, max_length=27, verbose_name='номер телефона котика'),
            preserve_default=False,
        ),
    ]
