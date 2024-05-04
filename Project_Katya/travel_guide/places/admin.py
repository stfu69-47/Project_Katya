from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Place, People


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'content', 'photo', 'post_photo']
    list_display = 'id', 'title', 'post_photo', 'time_created', 'is_published'
    list_display_links = 'id', 'title'
    ordering = ['time_created', 'title']
    list_editable = 'is_published',
    readonly_fields = ['post_photo',]
    search_fields = ['title']

    @admin.display(description='Изображение', ordering='title')
    def post_photo(self, place: Place):
        if place.photo:
            return mark_safe(f'<img src="{place.photo.url}" width=50>')
        return 'Без фото'


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'biography', 'place'
    list_display_links = 'id', 'name'
    list_editable = 'place',
    ordering = ['id', 'name']