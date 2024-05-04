# Generated by Django 4.2.1 on 2023-12-20 22:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0014_remove_place_places_plac_time_cr_992c04_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(5), django.core.validators.MaxLengthValidator(100)], verbose_name='URL'),
        ),
    ]
