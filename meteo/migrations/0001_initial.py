# Generated by Django 4.0.1 on 2022-01-31 19:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MeteoRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_time', models.DateTimeField(auto_now=True)),
                ('temperature', models.IntegerField(default=20, validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(-30)])),
                ('humidity', models.IntegerField()),
                ('wind_direction', models.IntegerField()),
            ],
        ),
    ]
