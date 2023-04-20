from django_filters import rest_framework as filter

from reviews.models import Title


class TitleFilter(filter.FilterSet):
    """
    Фильтр произведений по названию, жанру, категории и году.
    """

    name = filter.CharFilter(
        field_name='name',
        lookup_expr='contains'
    )
    genre = filter.CharFilter(
        field_name='genre__slug'
    )
    category = filter.CharFilter(
        field_name='category__slug'
    )
    year = filter.NumberFilter(
        field_name='year'
    )

    class Meta:
        model = Title
        fields = '__all__'
