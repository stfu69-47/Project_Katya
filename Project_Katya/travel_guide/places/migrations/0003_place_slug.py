# Generated by Django 4.2.1 on 2023-12-11 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_alter_place_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='slug',
            field=models.SlugField(blank=True, max_length=255),
        ),
    ]