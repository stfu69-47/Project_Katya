# Generated by Django 4.2.1 on 2023-12-14 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0011_uploadfiles_alter_people_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]