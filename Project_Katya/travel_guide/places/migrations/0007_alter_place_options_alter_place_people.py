# Generated by Django 4.2.1 on 2023-12-11 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_alter_place_people'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['-time_created'], 'verbose_name': 'Места', 'verbose_name_plural': 'Места'},
        ),
        migrations.AlterField(
            model_name='place',
            name='people',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='model_posts', to='places.people'),
        ),
    ]
