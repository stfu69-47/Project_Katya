# Generated by Django 4.2.1 on 2023-12-11 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_alter_place_options_alter_place_people'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='people',
        ),
        migrations.AddField(
            model_name='people',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='model_posts', to='places.place'),
        ),
    ]