from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.urls import reverse


class Place(models.Model):
    title = models.CharField(max_length = 255, verbose_name = 'Место')
    content = models.TextField(blank = True, verbose_name = 'Текст поста')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name = 'Время создания')
    time_updated = models.DateTimeField(auto_now=True, verbose_name = 'Время обновления')
    is_published = models.BooleanField(default = False, verbose_name = 'Опубликовано')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Места'
        verbose_name_plural = 'Места'
        ordering = ['time_created']
        indexes = [
            models.Index(fields=['-time_created'])
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


class People(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name = 'ФИО человека')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    biography = models.TextField(blank = True, verbose_name = 'Биография')
    place = models.ForeignKey(to=Place, on_delete=models.PROTECT,
                              related_name='model_posts', null=True, verbose_name = 'Место рождения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
            ]