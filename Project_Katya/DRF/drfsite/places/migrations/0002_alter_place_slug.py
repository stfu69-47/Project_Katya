# Generated by Django 4.2.8 on 2023-12-20 17:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True, validators=[django.core.validators.MinLengthValidator(5), django.core.validators.MaxLengthValidator(100)], verbose_name='URL'),
        ),
    ]