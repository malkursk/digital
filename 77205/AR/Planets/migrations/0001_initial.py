# Generated by Django 5.0.3 on 2024-03-12 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('orbital_period', models.IntegerField()),
                ('radius', models.FloatField()),
                ('weight', models.FloatField()),
            ],
        ),
    ]
