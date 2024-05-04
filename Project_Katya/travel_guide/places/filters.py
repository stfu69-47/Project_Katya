from django_filters import FilterSet, DateFilter, CharFilter
from .models import Place


class PlaceFilter(FilterSet):

    title = CharFilter(field_name='title',
                       lookup_expr='contains',
                       label='Место:')

    class Meta:
        model = Place
        fields = ('title',)