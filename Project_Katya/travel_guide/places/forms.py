from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible
from .models import Place, People


@deconstructible
class RussianValidator:
    ALLOWED_CHARS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧЩЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789- '
    code = 'russian'

    def __init__(self, message = None):
        self.message = message if message else 'Должны быть только русские буквы, цифры, дефис или пробел'

    def __call__(self, value, *args, **kwargs):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message, self.code)


class AddPostForm(forms.ModelForm):

    class Meta:
        model = Place
        fields = ['title', 'content', 'photo']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 4}),
        }
        labels = {'slug': 'URL'}


class AddPostFormPerson(forms.ModelForm):
    place = forms.ModelChoiceField(queryset=Place.objects.all(), label='Место рождения:', empty_label='Не выбрано')

    class Meta:
        model = People
        fields = ['name', 'biography', 'place']
        widgets = {
            'biography': forms.Textarea(attrs={'cols': 50, 'rows': 4}),
        }
        labels = {'slug': 'URL'}


class UploadFileForm(forms.Form):
    file = forms.ImageField(label='Файл')