# Generated by Django 5.0.1 on 2024-02-21 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='full_text',
            field=models.TextField(default='C2', verbose_name='полный текст новости'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='is_public',
            field=models.BooleanField(default='ДА', verbose_name='для открытой печати'),
        ),
    ]
